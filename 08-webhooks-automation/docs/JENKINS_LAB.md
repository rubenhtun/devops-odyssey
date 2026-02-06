# Lab 08: Webhook Automation

နောက်ဆုံးဖြစ်တဲ့ Lab 08 မှာ အဓိကလုပ်ဆောင်သွားမှာက **CI/CD Automation** ကို webhook သုံးပြီး automatic trigger လုပ်ဖို့အတွက်ပါ။ Lab 7 မှာတုန်းကလို **Jenkins Dashboard** ကနေ build လုပ်ဖို့အတွက် manual နှိပ်ခဲ့ရတာတွေ၊ configuration ချခဲ့ရတာတွေ အတိုင်းအတာတစ်ခုထိ ဆက်ရှိသေးမှာ ဖြစ်ပါတယ်။ ဒါပေမဲ့ အခု Lab မှာတော့ **GitHub Webhook** ကို အသုံးပြုသွားပါမယ်။ Developer ဘက်ကနေ `git push` အသစ်လုပ်လိုက်တာနဲ့ Jenkins က အလိုအလျောက် သိပြီးတော့ build လုပ်ပေးမယ့် **Fully Automated Pipeline** ကို တည်ဆောက်သွားမှာ ဖြစ်ပါတယ်။ ဒါပေမယ့် ဒီနေရာမှာ ခက်တာတစ်ခုက Jenkins က ကိုယ့်ရဲ့ စက်ထဲမှာပဲ ရှိနေတာပါ။ GitHub ကျတော့ internet ပေါ်မှာ ရှိနေပါတယ်။ အဲ့နှစ်ခုကို public address သုံးပြီး ဘယ်လိုချိတ်ဆက်ရမလဲဆိုတာ ဖြစ်လာပါတယ်။ အဲ့တော့ ngrok ကိုသုံးပြီး ဖြေရှင်းလိုက်ပါတယ်။

---

### 1. Infrastructure Setup (Ngrok & Webhook)

ပထမဆုံးအနေနဲ့ Jenkins က local စက်ထဲမှာ run နေတာဖြစ်လို့ GitHub ကနေ လှမ်းသိနိုင်ဖို့အတွက် **Ngrok** ကို အသုံးပြုပြီး tunnel ဖောက်ပေးရပါမယ်။

- **Ngrok Tunnel:** `ngrok http 8080`
- **GitHub Webhook Configuration:**
  - **Payload URL:** `https://<your-ngrok-url>/github-webhook/`
  - **Content type:** `application/json`
  - **Trigger:** Just the `push` event.

---

### 2. Automated Jenkinsfile

ဒီ `Jenkinsfile` မှာတော့ သတိထားမိတဲ့အတိုင်း Webhook trigger ပါဝင်လာပါတယ်။ ပြီးတော့ branch အလိုက် Port တွေကို if else နဲ့ စနစ်တကျ ခွဲခြားပေးထားပါတယ်။ Cleanup stage မှာလည်း error မတက်အောင် `|| true` ကိုပါ ထည့်အသုံးပြုထားပါတယ်။

```groovy
pipeline {
    agent any

    triggers {
        githubPush() // GitHub ကနေ push event လာတာနဲ့ build စတင်ဖို့အတွက်ပါ
    }

    environment {
        DOCKER_IMAGE = "rubenhtun/devops-odyssey-app"
    }

    stages {
        stage('Set Deploy Port') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        env.DEPLOY_PORT = '5000'
                    } else if (env.BRANCH_NAME == 'develop') {
                        env.DEPLOY_PORT = '5001'
                    } else {
                        env.DEPLOY_PORT = '5002'
                    }
                    echo "Deploy Port set to ${env.DEPLOY_PORT} for branch ${env.BRANCH_NAME}."
                }
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                echo "Cleaning up old containers..."
                sh "docker ps -q --filter name=${env.BRANCH_NAME}-container | xargs -r docker stop 2>/dev/null || true"
                sh "docker ps -a -q --filter name=${env.BRANCH_NAME}-container | xargs -r docker rm 2>/dev/null || true"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Image: ${DOCKER_IMAGE}:${env.BRANCH_NAME}"
                sh "docker build -t ${DOCKER_IMAGE}:${env.BRANCH_NAME} -f 08-webhooks-automation/Dockerfile ."
            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying branch ${env.BRANCH_NAME} to Port ${DEPLOY_PORT}..."
                sh """
                docker run -d \
                    --name ${env.BRANCH_NAME}-container \
                    -p ${DEPLOY_PORT}:5000 \
                    -e BRANCH_NAME=${env.BRANCH_NAME} \
                    -e BUILD_NUMBER=${env.BUILD_NUMBER} \
                    ${DOCKER_IMAGE}:${env.BRANCH_NAME}
                """
            }
        }

        stage('Health Check') {
            steps {
                script {
                    echo "Waiting for app to start..."
                    sh "sleep 5"
                    sh "curl -f http://localhost:${DEPLOY_PORT}"
                    echo "Health Check Passed!"
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
```

---

### 3. Key Improvements in Lab 08

1. **GitHub Push Trigger:** `triggers { githubPush() }` ကို ထည့်သွင်းထားတဲ့အတွက် manual build လုပ်စရာ မလိုတော့ပါဘူး။
2. **Robust Cleanup:** Container ဟောင်းတွေကို ရှင်းထုတ်တဲ့အခါမှာ pipeline မရပ်သွားအောင် filter နဲ့ error handling ကိုပါ ပိုကောင်းသွားအောင် ပြင်လိုက်တာပါ။
3. **Workspace Management:** နောက်ဆုံးမှာ build တစ်ခုပြီးတိုင်း server ပေါ်မှာ နေရာရှုပ်ပွမသွားရအောင် `cleanWs()` ကို အပိုဆောင်း ထည့်လိုက်ပါတယ်။

---

### 4. Verification & Results

အောင်မြင်မအောင်မြင် သိဖို့ကျရင်တော့ အောက်ပါအတိုင်း စစ်လို့ရပါတယ်။

1. **Push Test:** ကိုယ့်ရဲ့ code ကိုပြင်ပြီး `git push` လုပ်လိုက်တာနဲ့ Jenkins မှာ build တစ်ခု အလိုအလျောက် စတက်လာရပါမယ်။
2. **Webhook Logs:** GitHub settings ထဲက Webhook section မှာ delivery status ဟာ အစိမ်းရောင် အမှန်ခြစ်လေး ပြနေရပါမယ်။
3. **Multi-Environment View:**
   - **Main:** `http://localhost:5000`
   - **Develop:** `http://localhost:5001`
   - **Others:** `http://localhost:5002`
