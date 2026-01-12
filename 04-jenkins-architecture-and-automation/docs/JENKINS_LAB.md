# Jenkins Automation Lab

### 1. Jenkins Home Investigation

ဒီအပိုင်းမှာတော့ `Jenkins` home ရဲ့ အတွင်းပိုင်းပုံစံကို အနည်းငယ်လောက်ပဲ လေ့လာသွားမှာမို့လို့
ပထမဆုံးအနေနဲ့ terminal မှာ အောက်က command တွေကို သုံးပေးရမှာ ဖြစ်ပါတယ်။
`Docker Compose` ဖိုင်ကတော့ `Lesson 3` ကလို တူတူထားသွားမှာ ဖြစ်ပါတယ်။

```bash
# ထုံးစံအတိုင်း container ကို စ run ဖို့ docker-compose ကို စမောင်းပေးရမှာ ဖြစ်ပါတယ်။
docker-compose up -d

# Container ID သို့မဟုတ် name ကို ကြည့်ဖို့လိုလာရင်။
docker ps

# Docker container ထဲကို စဝင်ပါမယ်။
docker exec -it <container_name> bash

# root access ရပြီဆိုရင် ဒီ command သုံးပြီး Jenkins home directory ထဲ ဝင်လို့ရပါပြီ။
ls /var/jenkins_home
```

### 2. Jenkins Home Structure

`Jenkins` home folder ထဲမှာတော့ internal files တွေ ကိုယ်စီရှိနေတာကို တွေ့ရမှာပဲ ဖြစ်ပါတယ်။
အဲ့ဒီအားလုံးထဲက အရေးကြီးတဲ့ ဖိုင်နဲ့ folder တချို့လောက်ကိုပဲ ရှင်းပြသွားပါမယ်။

- **`config.xml`** : `Jenkins` တစ်ခုလုံးရဲ့ settings နဲ့ configurations တွေ ရှိတဲ့နေရာပါ။

- **`jobs/`** : `Jenkins` ပေါ်မှာ ဆောက်ထားခဲ့သမျှ project configurations နဲ့ build history logs တွေ ဒီအထဲမှာ ရှိပါတယ်။

- **`plugins/`** : `Jenkins` မှာ သွင်းထားတဲ့ plugins ဖိုင်တွေ အတွက်ပါ။

- **`workspace/`** : `Jenkins` ရဲ့ ပုံမှန်လုပ်ဆောင်ပုံအရဆိုရင် `GitHub` ကနေ code တွေ ဆွဲချပြီး ယာယီ အလုပ်လုပ်တဲ့နေရာ ဖြစ်ပါတယ်။

### 3. Advanced Job Setup

ဒီ Lab မှာတော့ `Freestyle job` ကိုပဲ တချို့ manually configure လုပ်သွားရမှာ ဖြစ်ပါတယ်။ သက်ဆိုင်ရာ အပိုင်းသုံးပိုင်းလောက်ကိုပဲ အဓိကထားပြီး လုပ်သွားပါမယ်။

- **Parameters:** Dynamic build လုပ်နိုင်ဖို့အတွက်ဆိုရင် `BRANCH_NAME` နဲ့ `ENV` တို့လို parameters တွေကို ကိုယ်တိုင် configure လုပ်ရမှာတွေ ရှိပါတယ်။

- **Automation Trigger:** `Lesson 3` မှာလို `Poll SCM` လိုဟာမျိုးကို အသုံးပြုပြီးတော့ `H/2 * * * *` နှစ်မိနစ်တစ်ခါ `GitHub` ဆီကို သွားပြီး code အသစ် push လုပ်ထားတာ ရှိမရှိ စစ်ဆေးခိုင်းထားလို့လည်း ရပါတယ်။

- **Git Integration:** Branch specifier နေရာမှာဆိုလည်း အပေါ်ကသတ်မှတ်ထားခဲ့တဲ့ `${BRANCH_NAME}` ကို သုံးပြီး ကိုယ်စိတ်ကြိုက် branch ကို build လုပ်ရပါသေးတယ်။

### 4. Workspace Cleanup Strategy

သတိထားရမှာတစ်ခုက build တစ်ခု ပြီးဆုံးတိုင်း workspace ထဲမှာ code တွေ ပုံလာမှာ ဖြစ်ပါတယ််။ အဲ့တာကြောင့် `Post-build` အဆင့်မှာ cleanup လုပ်လို့ ရပါတယ််။ ဒါပေမဲ့ `Docker image` လို နောက်ဆုံးရလာတဲ့ artifacts တွေကို `Docker Hub` မဟုတ်ရင် Repository တစ်ခုခုဆီကို အရင်ပို့ပြီးမှသာ workspace ကို cleanup လုပ်သင့်ပါတယ်။ အဲ့လိုသာ မလုပ်ရင် build လုပ်ပြီးသား `Docker image` တွေ ပျောက်သွားနိုင်လို့ပါ။

```bash
rm -rf *
```
