# Jenkins Automation Lab

### 1. Jenkins Home Investigation

ဒီအပိုင်းမှာတော့ `Jenkins` home ရဲ့ အတွင်းပိုင်းပုံစံကို အနည်းငယ်လောက််ပဲ လေ့လာသွားမှာမို့လို့
ပထမဆုံးအနေနဲ့ terminal မှာ အောက်က command တွေကို သုံးပေးရမှာ ဖြစ်ပါတယ်။
Docker Compose ဖိုင်ကတော့ Lesson 3 ကလို တူတူထားသွားမှာ ဖြစ်ပါတယ်။

```bash
# ထုံးစံအတိုင်း container ကို စ run ဖို့ docker-compose ကို စမောင်းပေးရမှာ ဖြစ်ပါတယ်။
docker-compose up -d

# Container ID မဟုတ် name ကို ကြည့်ဖို့လိုလာရင်။
docker ps

# Docker container ထဲကို စဝင်ပါမယ်။
docker exec -it <container_name> bash

# root access ရပြီဆိုရင် ဒီ command သုံးပြီး Jenkins home directory ထဲ ဝင်လို့ရပါပြီ
ls /var/jenkins_home
```

### 2. Jenkins Home Internal System

Home folder ထဲမှာတော့ internal files တွေ ကိုယ်စီ ရှိနေတာကို တွေ့ရမှာပဲ ဖြစ်ပါတယ်။
အဲ့ဒီအားလုံးထဲက အရေးကြီးတဲ့ ဖိုင်နဲ့ folder တချို့ကိုပဲ ရှင်းပြသွားပါမယ်။

- config.xml : Jenkins တစ်ခုလုံးရဲ့ settings နဲ့ configurations တွေ ရှိတဲ့နေရာပါ။

- jobs/ folder : Jenkins ပေါ်မှာ ဆောက်ထားခဲ့သမျှ project configurations နဲ့ build history logs တွေ ဒီအထဲမှာ ရှိပါတယ်။

- plugins/ folder : Jenkins မှာ သွင်းထားတဲ့ plugin ဖိုင်တွေ အတွက်ပါ။

- workspace/ folder : Jenkins အနေအားဖြင့် GitHub ကနေ code တွေ ဆွဲချပြီး ယာယီ အလုပ်လုပ်တဲ့နေရာ ဖြစ်ပါတယ်။

### 3. Advanced Job Setup

ဒီ Lab မှာတော့ Freestyle job ကိုပဲ တချို့ manually set up လုပ်သွားရမှာ ဖြစ်ပါတယ်။

- **Parameters:** Dynamic build လုပ်နိုင်ဖို့အတွက်ဆိုရင် `BRANCH_NAME` နဲ့ `ENV` တို့လို parameters တွေကို ကိုယ်တိုင် configure လုပ်ရမှာတွေ ရှိမှာဖြစ်ပါတယ်။
- **Automation Trigger:** Lesson 3 မှာလို `Poll SCM` လိုဟာမျိုးကို အသုံးပြုပြီးတော့ `H/2 * * * *` နှစ်မိနစ်တစ်ခါ GitHub ဆီကို သွားပြီး code အသစ် push လုပ်ထားတာ ရှိမရှိ စစ်ဆေးခိုင်းထားလို့ ရပါတယ်။
- **Git Integration:** Branch specifier နေရာမှာဆိုလည်း `${BRANCH_NAME}` ကို သုံးပြီး ကိုယ်စိတ်ကြိုက် branch ကို build လုပ်ရပါသေးတယ်။

### 4. Workspace Cleanup Strategy

Build တစ်ခု ပြီးဆုံးတိုင်း workspace ထဲတွင် code များ ပုံမနေစေရန် Post-build step တွင် အောက်ပါအတိုင်း ရှင်းလင်းခဲ့သည်-
`rm -rf *`
_သတိပြုရန်: အရေးကြီးသော artifacts များကို အပြင်သို့ (S3 သို့မဟုတ် Docker Hub) အရင်ပို့ပြီးမှသာ ရှင်းလင်းသင့်သည်။_
