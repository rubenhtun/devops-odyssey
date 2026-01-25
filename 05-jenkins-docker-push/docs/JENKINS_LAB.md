# Jenkins to Docker Hub CI/CD Lab

အတိုချုံး မိတ်ဆက်ရရင် ဒီ Lab ရဲ့ အဓိက ရည်ရွယ်ချက်ကတော့ **Python Flask app** လေးတစ်ခုကို **GitHub** ပေါ် တင်ပါမယ်။ **GitHub repo** မှာ **code changes** တစ်ခုခု ဖြစ်တာနဲ့ **Jenkins** ကနေ အလိုအလျောက် သိရပါမယ်။ **Jenkins** ထဲမှာ Project ကို **Build Now** လုပ်လိုက်တာနဲ့ image ကို တည်ဆောက်ပြီး **registry** ဖြစ်တဲ့ **Docker Hub** ပေါ်ကို **Docker image** အဖြစ် ပို့ပေးမှာ ဖြစ်ပါတယ်။ Build လုပ်လိုက်တိုင်းမှာ ထွက်လာတဲ့ image တွေက version မတူကြပါဘူး။ ဒါပေမယ့် **Jenkins** က နောက်ဆုံး version ကို သုံးပြီး ကိုယ့်ကွန်ပျူတာရဲ့ **localhost:5000** ပေါ်မှာ **container** အဖြစ် အလိုအလျောက် ပြန် deploy ပေးသွားမှာ ဖြစ်ပါတယ်။

---

### 1. Credentials Configuration

ပထမဆုံးအနေနဲ့ **Docker Hub** ကို image လှမ်းပို့ဖို့အတွက်ဆိုရင် credentials အနေနဲ့ username နဲ့ password ကို ထည့်သုံးရမှာဖြစ်ပါတယ်။

- **Jenkins credentials:**
- **Kind:** Username with password
- **Username:** `rubenhtun`
- **Password:** `********`
- **ID:** `docker-hub-creds`

---

### 2. Source Code Management

**Jenkins job** ကို **GitHub repository** နဲ့ ချိတ်ဆက်ပြီး code တွေကို အလိုအလျောက် `jenkins_home` ထဲကို ဆွဲယူဖို့ သတ်မှတ်ထားဖို့ လိုပါမယ်။

- **Repository URL:** `https://github.com/rubenhtun/devops-odyssey.git`
- **Branch specifier:** `*/main`
- **Sub-directory:** code တွေက သီးသန့် folder အောက်မှာ ရှိနေတဲ့အတွက် build လုပ်တဲ့အခါ `05-jenkins-docker-push` folder ထဲကို အရင်ဝင်ဖို့ လိုပါတယ်။

---

### 3. Build Environment & Bindings

ဒီအဆင့်မှာတော့ shell script ထဲမှာ **Docker Hub** username နဲ့ password ကို variable အနေနဲ့ လုံလုံခြုံခြုံ သုံးလို့ရအောင် **bindings** လုပ်တဲ့သဘောပါ။

- **Username variable:** `DOCKER_USERNAME`
- **Password variable:** `DOCKER_PASSWORD`

---

### 4. Execute Shell

**Jenkins** ကနေ build steps တွေကို အလိုအလျောက် လုပ်ဆောင်နိုင်ဖို့အတွက် shell script ထဲမှာ ကိုယ် instructions ပေးချင်တာကို အစဉ်လိုက် ထည့်ပေးရပါမယ်။

```bash
# Build လုပ်လုပ်ချင်းမှာပဲ lab 5 folder ထဲ ဝင်ဖို့အတွက်ပါ
cd 05-jenkins-docker-push

# Build version နံပါတ်နဲ့ပါ တွဲပြီး Docker image build လုပ်တာပါ
docker build -t rubenhtun/odyssey-flask-app:${BUILD_NUMBER} .
docker build -t rubenhtun/odyssey-flask-app:latest .

# Docker Hub login ဝင်တာပါ
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin

# Image တွေကို Docker Hub ပေါ်ကို push လုပ်တာပါ
docker push rubenhtun/odyssey-flask-app:${BUILD_NUMBER}
docker push rubenhtun/odyssey-flask-app:latest

# Container အဟောင်းကို ဖျက်ပြီး အသစ်ပြန်မောင်းတာပါ
docker rm -f odyssey-flask-app || true
docker run -d --name odyssey-flask-app -p 5000:5000 rubenhtun/odyssey-flask-app:latest
```

---

### 5. Verification

အပေါ်က pipeline တစ်ခုလုံး ပြီးသွားပြီဆိုရင် အောင်မြင်မှုရှိမရှိ စစ်ဆေးလို့ရပါမယ်။

1. **Jenkins console:** `Finished: SUCCESS` ဖြစ်နေရပါမယ်။
2. **Docker Hub:** repository ထဲမှာ tag နံပါတ်အသစ်နဲ့ image ရောက်နေရပါမယ်။
3. **localhost:** browser မှာ `http://localhost:5000` ကို ခေါ်ကြည့်တဲ့အခါ ရေးထားတဲ့ **Flask app** စာမျက်နှာလေး ပေါ်လာရပါမယ်။
