from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# from .models import lungcancerdata

# Create your views here.
# def home(request):
#     return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        last = request.POST["lname"]
        uname = request.POST["uname"]
        emailid = request.POST['email']
        password1 = request.POST["PASSWORD"]
        password2 = request.POST["cpasswrd"]
        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=emailid).exists():
                messages.info(request,"Email Exists")
            else:
                u=User.objects.create_user(first_name=first,last_name=last,email=emailid,username=uname,password=password2)
                u.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return render(request,"register.html")
    else:
        return render(request,"register.html")

    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        u1=request.POST['uname']
        p1=request.POST['PASSWORD']
        user1=auth.authenticate(username=u1,password=p1)
        if user1 is not None:
            auth.login(request,user1)
            return redirect('about')
        else:
            messages.info(request,"Invalid username or Password!")
            return render(request,"login.html")
    return render(request,"login.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def doctor(request):
    return render(request,"doctor.html")

def testimonial(request):
    return render(request,"testimonial.html")

def treatment(request):
    return render(request,"treatment.html")

def LungPrediction(request):
    if (request.method == 'POST'):
        age=request.POST['age']
        gender=request.POST['gender']
        airpollution=request.POST['airpollution']
        alcoholuse=request.POST['alcoholuse']
        dustallergy = request.POST['dustallergy']
        occupationalhazards=request.POST['occupationalhazards']
        geneticrisk= request.POST['geneticrisk']
        chroniclungdisease=request.POST['chroniclungdisease']
        balanceddiet=request.POST['balanceddiet']
        obesity= request.POST['obesity']
        smoking=request.POST['smoking']
        passivesmoker=request.POST['passivesmoker']
        chestpain=request.POST['chestpain']
        coughingofblood=request.POST['coughingofblood']
        fatigue=request.POST['fatigue']
        weightloss=request.POST['weightloss']
        shortnessofbreath=request.POST['shortnessofbreath']
        wheezing=request.POST['wheezing']
        swallowingdifficulty=request.POST['swallowingdifficulty']
        clubbingoffingernails = request.POST['clubbingoffingernails']
        frequentcold=request.POST['frequentcold']
        dry_cough = request.POST['drycough']
        snoring= request.POST['snoring']

        df = pd.read_csv(r"static/dataset/Lung_cancer.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.heatmap(df.isnull())
        # plt.show()
        x=df.drop(["Age","Level"],axis=1)
        Y=df["Level"]
        from sklearn.model_selection import train_test_split
        x_train,x_test,Y_train,Y_test=train_test_split(x,Y,test_size=0.40)
        from sklearn.ensemble import RandomForestClassifier
        ran=RandomForestClassifier()
        ran.fit(x_train,Y_train)
        pred=ran.predict(x_test)
        plt.plot(x_test,Y_test)
        # plt.show()
        
        plt.plot(x_test,pred)
    
        # plt.show()


        X_train = df[['Age','Gender','Air_Pollution','Alcohol_Use','Dust_Allergy','OccuPational_Hazards','Genetic_Risk','Chronic_Lung_Disease','Balanced_Diet','Obesity',
                      'Smoking','Passive_Smoker','Chest_Pain','Coughing_Of_Blood','Fatigue','Weight_Loss','Shortness_Of_Breath','Wheezing','Swallowing_Difficulty','Clubbing_Of_Finger_Nails',
                      'Frequent_Cold','Dry_Cough','Snoring']]
        y_train = df[['Level']]
        ran = RandomForestClassifier()
        ran.fit(X_train,y_train)
        
        prediction = ran.predict([[age,gender,airpollution,alcoholuse,dustallergy,occupationalhazards,geneticrisk,chroniclungdisease,balanceddiet,obesity,smoking,passivesmoker,chestpain,coughingofblood,fatigue,
                                   weightloss,shortnessofbreath,wheezing,swallowingdifficulty,clubbingoffingernails,frequentcold,dry_cough,snoring]])
        
        from .models import LungCancer
        lungcancer=LungCancer.objects.create(Age=age,Gender=gender,Air_Pollution=airpollution,Alcohol_Use=alcoholuse,Dust_Allergy=dustallergy,OccuPational_Hazards=occupationalhazards,Genetic_Risk=geneticrisk,
                                                  Chronic_Lung_Disease=chroniclungdisease,Balanced_Diet=balanceddiet,Obesity=obesity,Smoking=smoking,Passive_Smoker=passivesmoker,Chest_Pain=chestpain,Coughing_Of_Blood=coughingofblood,
                                                  Fatigue=fatigue,Weight_Loss=weightloss,Shortness_Of_Breath=shortnessofbreath,Wheezing=wheezing,Swallowing_Difficulty=swallowingdifficulty,Clubbing_Of_Finger_Nails=clubbingoffingernails,
                                                  Frequent_Cold=frequentcold,Dry_Cough=dry_cough,Snoring=snoring)
        lungcancer.save()
        return render(request,'LungPrediction.html',
                      {"lungcancer": prediction,'age':age,'gender':gender,'airpollution':airpollution,'alcoholuse':alcoholuse,'dustallergy':dustallergy,'occupationalhazards':occupationalhazards,'geneticrisk':geneticrisk,'chroniclungdisease':chroniclungdisease,'balanceddiet':balanceddiet,'obesity':obesity,'smoking':smoking,'passivesmoker':passivesmoker,'chestpain':chestpain,'coughingofblood':coughingofblood,'fatigue':fatigue,
                                   'weightloss':weightloss,'shortnessofbreath':shortnessofbreath,'wheezing':wheezing,'swallowingdifficulty':swallowingdifficulty,'clubbingoffingernails':clubbingoffingernails,'frequentcold':frequentcold,'dry_cough':dry_cough,'snoring':snoring })
    else:
        return render(request, 'LungPrediction.html')
