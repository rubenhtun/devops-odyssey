# Jenkins Multibranch Pipeline

Lab 07 မှာ အဓိကလုပ်ဆောင််သွားမှာကတော့ **Multibranch Pipeline** စနစ်ကို တည်ဆောက်ဖို့ပါ။ အရင် Lab 6 မှာတုန်းက `main` branch တစ်ခုတည်းကိုပဲ automation လုပ်ခဲ့တာပါ။ အခု Lab မှာတော့ GitHub ပေါ်မှာရှိတဲ့ **Branch အားလုံး (main, develop, feature-login)** ကို Jenkins က အလိုအလျောက် ရှာဖွေ indexing လုပ်ပြီး branch တစ်ခုချင်းစီအတွက် pipeline တစ်ခုစီကို အလိုအလျောက် တည်ဆောက်ပေးသွားမှာ ဖြစ်ပါတယ်။ ထူးခြားချက်အနေနဲ့တော့ branch နာမည်အလိုက် **Dynamic Port Mapping (5000, 5001, 5002)** ကိုသုံးပြီး ပြိုင်တူ deployment လုပ်သွားရမှာ ဖြစ်ပါတယ်။

---

### 1. Project Directory Structure

ဒီတစ်ခါ ပိုရှင်းသွားအောင်လို့ HTML view ကို template အနေနဲ့ သီးသန့်ထည့်သွင်းရေးထားပါတယ်။ Folder structure ကိုလည်း code တွေနဲ့ configuration ဖိုင်တွေ မရောရအောင် ပိုသပ်သပ်ရပ်ရပ်လေးဖြစ်အောင် ခွဲထားပါတယ်။

```
07-multibranch-pipeline/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── docs/
│   ├── README.md
│   ├── NOTES.md
│   ├── JENKINS_LAB.md
│   └── diagrams/
│       ├── pipeline-flow.svg
│       └── infrastructure.svg
├── .dockerignore
├── Dockerfile
└── Jenkinsfile
```

---

### 2. Multibranch Pipeline Configuration

ဒီတစ်ခါတော့ **Jenkins Dashboard** မှာ project အသစ်ဆောက်တဲ့အခါ "Pipeline" အစား **"Multibranch Pipeline"** ကို ရွေးချယ်ရပါမယ်။

- **Project Name:** `devops-odyssey-multibranch`
- **Branch Sources:** Git
- **Repository URL:** `https://github.com/rubenhtun/devops-odyssey.git`
- **Credentials:** `github-creds` (Private repo ဆိုရင် token ယူပြီး သုံးဖို့ပါ)
- **Build Configuration (Mode):** by Jenkinsfile
- **Script Path:** `07-multibranch-pipeline/Jenkinsfile`

---

### 3. Dynamic Environment Variables

Jenkinsfile ထဲမှာ သူ့ဟာနဲ့သူ branch အလိုက် လွယ်လွယ်ကူကူ ခွဲခြားနိုင်အောင်ဆိုပြီး dynamic variable တွေကို သုံးထားပါတယ်။

- **IMAGE_TAG:** `${env.BRANCH_NAME}-${env.BUILD_NUMBER}`
- **DEPLOY_PORT:** Branch အလိုက် port တွေ မတူညီအောင်ပါ
  - `main` → 5000
  - `develop` → 5001
  - `feature-login` → 5002

---

### 4. Multibranch Jenkinsfile Logic

ဒီ pipeline ကို ကြည့်လိုက်ရင် branch အလိုက် image build လုပ်မယ်။ **Docker Hub** ဆီကို image အသီးသီးကို push လုပ်မယ်။ ပြီးတော့ နောက်ဆုံးအနေနဲ့ container နာမည်တွေကိုလည်း deploy လုပ်တဲ့အခါ မတူညီအောင် branch name နဲ့ ခွဲထားလိုက်ပါတယ်။

```groovy
pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDS_ID = 'docker-hub-creds'
        DOCKER_IMAGE = "rubenhtun/devops-odyssey-app"
        IMAGE_TAG = "${BRANCH_NAME}-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo "Checking out code from GitHub..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dir('07-multibranch-pipeline') {
                        echo "Building Image: ${DOCKER_IMAGE}:${IMAGE_TAG}"
                        sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
                        sh "docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Logging in to Docker Hub and pushing image..."
                script {
                    withCredentials([usernamePassword(
                      credentialsId: "${DOCKER_HUB_CREDS_ID}",
                      passwordVariable: 'DOCKER_HUB_PASSWORD',
                      usernameVariable: 'DOCKER_HUB_USERNAME'
                      )]) {
                        sh "echo \$DOCKER_HUB_PASSWORD | docker login -u \$DOCKER_HUB_USERNAME --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"

                        if (env.BRANCH_NAME == 'main') {
                            sh "docker push ${DOCKER_IMAGE}:latest"
                        }
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    def PORT_MAP = [
                      'main': 5000,
                      'develop': 5001,
                      'feature-login': 5002
                    ]

                    def DEPLOY_PORT = PORT_MAP.get(env.BRANCH_NAME) ?: 5003

                    echo "Deploying branch ${env.BRANCH_NAME} to Port ${DEPLOY_PORT}..."
                    CONTAINER_NAME = "devops-odyssey-app-${BRANCH_NAME}"
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    sh """
                        docker run -d --name ${CONTAINER_NAME} \
                        -p ${DEPLOY_PORT}:5000 \
                        -e BRANCH_NAME=${env.BRANCH_NAME} \
                        -e BUILD_NUMBER=${env.BUILD_NUMBER} \
                        ${DOCKER_IMAGE}:${IMAGE_TAG}
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace and logging out from Docker Hub..."
            sh "docker logout"
            cleanWs()
        }
        success {
            echo "Successfully deployed branch ${env.BRANCH_NAME}!"
        }
        failure {
            echo "Pipeline failed. Please check the Console Output."
        }
    }
}
```

---

### 5. Verification & Results

ထုံးစံအတိုင်း build လုပ်တာအားလုံး ပြီးဆုံးသွားပြီဆိုရင် results တွေကို စစ်လို့ရပါပြီ။

1. **Multibranch View:** Jenkins Dashboard မှာ branch သုံးခုလုံးအတွက် သီးသန့် pipeline status တွေကို တွေ့ရပါမယ်။ အဲဒီထဲကနေ branch တစ်ခုချင်းစီရဲ့ build stage ကို ကြည့်လည်းရပါသေးတယ်။
2. **Docker Hub Tags:** Repository ထဲဆိုရင်လည်း `main-x`, `develop-x`, `feature-login-x` စတဲ့ မတူညီတဲ့ tag အသစ်တွေ ရောက်နေရပါမယ်။
3. **Multi-Port Access:**
   - `http://localhost:5000` (Main Branch App)
   - `http://localhost:5001` (Develop Branch App)
   - `http://localhost:5002` (Feature Login Branch App)
