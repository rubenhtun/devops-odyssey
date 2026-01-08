# Docker & CI/CD Practical Commands Cheatsheet

### 1. Building the Artifact

```bash
# ဒီ command ကျတော့ application ကို run ဖို့လိုလာတဲ့အခါ environment တွေအကုန်ပါတဲ့
# Docker Image (artifact) တစ်ခုကို တည်ဆောက်ပေးတာပါ။
# Command မှာပါတဲ့ အစိတ်အပိုင်းတွေကို ထပ်ခွဲပြီးပြောရရင် username ကတော့ ကိုယ့်ရဲ့ Docker Hub username ပါ။
# devops-odyssey ကတော့ Repository/App name ပါ။
# v1.0 ကတော့ version နံပါတ််ပါ။
# နောက်ဆုံး '.' ကတော့ လက်ရှိရောက်နေတဲ့ directory ကို ပြောတာဖြစ်ပါတယ်။
docker build -t username/devops-odyssey:v1.0 .
```

### 2. Publishing to Registry

```bash
# Image ကို build လုပ်ပြီးသွားပြီဆိုရင်
# local ကနေ Docker Hub ပေါ်ကို image upload လုပ်ဖို့ အရင်ဆုံး login ဝင်ရပါမယ်။
docker login

# နောက််ဆုံး 'push' command ကိုသုံးပြီး image ကို upload လုပ်လိုက်တာပါ။
docker push username/devops-odyssey:v1.0
```

### 3. Running the Application (Deployment)

```bash
# ဒီ command ကျသွားရင််တော့ docker-compose.yml ဖိုင်မှာ သတ်မှတ်ထားတဲ့ services တွေပေါ်မူတည်ပြီး background မှာ run ပေးမှာ ဖြစ််ပါတယ်။
# လက်ရှိမှာတော့ web app, database container နှစ်ခုကိုပဲ တစ်ခါတည်း run လုပ်ပေးသွားမှာ ဖြစ်ပါတယ််။
docker-compose up -d

# down နဲ့ up ဆိုပြီး တွဲရေးလိုက်တာက ဖိုင်တစ်ခုရဲ့ configuration ပြောင််းထားလိုက်ရင် ပြန်် restart လုပ်လို့ရအောင်် ဆိုပြီးပါ။
docker-compose down && docker-compose up -d

# ဒီ command ကိုသုံးပြီး လက်ရှိမှာ run နေတဲ့ containers တွေရဲ့ logs ကို real-time ပုံစံနဲ့ ကြည့်လို့ရအောင်လို့ပါ။
docker-compose logs -f
```

### 4. Cleanup & Maintenance

```bash
# ဆက်မသုံးဖြစ််တော့တဲ့ stopped containers တွေကြောင့် disk space မပြည့်အောင်ပါ။
docker container prune

# ဘယ် container ကမှ ဆက်မသုံးတော့တဲ့ images တွေကို ဖယ်ရှားပစ်တာပါ။
docker image prune -a
```
