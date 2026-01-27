# 🐳 Docker Commands Cheatsheet

### 1. Image Management

```bash
# Python အတွက် Docker Hub ကနေ image ရှာချင်တယ်ဆိုရင် `search` command ကို သုံးပြီး ရှာလို့ရပါတယ်။
docker search python

# ကိုယ်က Docker Hub ကနေ version နံပါတ် အတိအကျရှိတဲ့ image ကိုပဲ
# ကိုယ့်ရဲ့ကွန်ပျူတာထဲကို ဒေါင်းလုဒ်ဆွဲချချင်ရင်တော့ `pull` command ကို သုံးရပါတယ်။
docker pull python:3.9-slim

# အဲ့တာအပြင် ကိုယ့်ကွန်ပျူတာထဲမှာ ရှိနေတဲ့ Docker images အကုန်လုံးကို
# ကြည့်ချင်တယ်ဆိုတဲ့အခါကျတော့ အောက်က command ကို သုံးရမှာဖြစ်ပါတယ်။
docker images

# `rmi` ဆိုတာက remove image ရဲ့ အတိုကောက်ပါ။
# ကိုယ်ဖျက်ချင်တဲ့ image ကို image ID နဲ့ဖြစ်ဖြစ်၊ name နဲ့ဖြစ်ဖြစ် ဖျက်လို့ရပါတယ်။
docker rmi <image_id_or_name>
```

### 2. Container Lifecycle

```bash
# ဒီ command ဟာကျတော့`python-app` ဆိုတဲ့ image ကနေ
# `devops-odyssey-app` ဆိုတဲ့ container တစ်ခုကို ဖန်တီးယူလိုက်တာ ဟုတ်ပါတယ်။
# တပြိုင်တည်းမှာ ကိုယ့်ကွန်ပျူတာရဲ့ local port 3000 ကို container port 5000 နဲ့ ချိတ်ပေးလိုက်ပြီး
# နောက်ခံ (detached mode) နဲ့ run လုပ်ပေးတာ ဖြစ်ပါတယ်။
docker run -d --name devops-odyssey-app -p 3000:5000 python-app

# Docker ဟာ containerization နည်းပညာကို အသုံးပြုပြီး အလုပ်လုပ်တာဖြစ်တဲ့အတွက်
# လက်ရှိ run ဖြစ်နေတဲ့ containers တွေကို ကြည့်ချင်တယ်ဆိုရင်
# `docker ps` command ကို run ရုံနဲ့ ရပါတယ်။
docker ps

# လက်ရှိ run ဖြစ်နေတဲ့ container တွေအပြင်
# ရပ်ထားပြီးသား (stopped / exited) ဖြစ်တဲ့ container တွေကိုပါ
# အားလုံးကို ပြပေးတဲ့ command ပါ။
docker ps -a

# လက်ရှိ run ဖြစ်နေတဲ့ container တစ်ခုကို ရပ်တန့်ချင်ရင်တော့ 'stop' ကို သုံးရုံပါပဲ။
docker stop <container_id_or_name>

# အရင်က ရပ်ထားခဲ့တဲ့ container တစ်ခုကို ပြန်အသုံးပြုချင်တဲ့အခါ 'start' command ကို သုံးလိုက်ရုံပါပဲ။
docker start <container_id_or_name>

# အလုပ်မလုပ်တော့တဲ့ ဒါမှမဟုတ် ရပ်ထားပြီးသား container တစ်ခုကို စနစ်ထဲကနေ လုံးဝအပြီးအပိုင် ဖယ်ရှားပစ်ဖို့အတွက်ပါ။
docker rm <container_id_or_name>
```

### 3. Inspection and Debugging

```bash
# ပုံမှန်အားဖြင့်ဆိုရင် container တစ်ခု အလုပ်လုပ်နေတဲ့အချိန်မှာ ထွက်လာတဲ့ output logs တွေဆိုတာ ရှိပါတယ်။
# အဲ့ဒီ logs တွေကို ကြည့်ဖို့အတွက်ဆိုရင် ဒီ command ကိုပဲ သုံးပါတယ်။
docker logs <container_id_or_name>

# Container run နေတဲ့အချိန်မှာပဲ အထဲကို terminal ပုံစံနဲ့ တိုက်ရိုက်ဝင်ပြီး
# command တွေကို ကိုယ်တိုင် run လုပ်ချင်တဲ့အခါမျိုးမှာ သုံးဖို့အတွက်ပါ။
docker exec -it <container_id_or_name> /bin/bash

# Container နဲ့ဆိုင်တဲ့ configuration, network, volume စသဖြင့်
# အသေးစိတ် အချက်အလက်တွေကို JSON format ပုံစံနဲ့
# တစ်စုတစ်စည်းတည်း ကြည့်ဖို့လိုလာတဲ့အခါ 'inspect' command ကို မမေ့ဖို့ပါပဲ။
docker inspect <container_id_or_name>
```

### 4. System Maintenance

```bash
# 'prune' ဆိုတာက မလိုတဲ့အပိုင်းတွေကို ဖယ်ရှားပစ်ဖို့အတွက်ပါ။
# ဆိုလိုတာက လက်ရှိမှာ ဆက်မသုံးဖြစ််တော့တဲ့ stopped containers တွေ၊
# အသုံးမလိုတော့တဲ့ networks တွေ၊
# dangling ဖြစ်တဲ့ images တွေလို မလိုအပ်တဲ့ Docker data အားလုံးကို
# ဖယ်ရှားပစ်လိုက်တော့မယ်ဆိုတဲ့ သဘောပါ။
docker system prune
```
