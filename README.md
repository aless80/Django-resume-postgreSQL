Credits to [ckelly](https://github.com/ckelly) on this repository: [django-resume](https://github.com/ckelly/django-resume) . 
The project was not working on python 3 and Django 2.0.2 so I decided to rebuild it. I will probably work on it. 

Fire up a shell and create your resume with commands similar to the following ones: 
```
python3 manage.py shell

import datetime

from resume.models import PersonalInfo
pi=PersonalInfo.objects.create(email='AlessandroMarin80@gmail.com', region='MA', first_name= 'Alessandro', locality='Boston', last_name='Marin')
pi.title='Developer'
pi.linkedin='https://www.linkedin.com/in/alessandromarin80/'
pi.github='https://github.com/aless80'
pi.site='http://www.somesite.com'
pi.save()
pi.__dict__  #print the fields

from resume.models import Language
l1=Language.objects.create(language='English',level='professional')
l2=Language.objects.create(language='Dutch',level='professional')
l2.ordering=2
l1.save()
l2.save()

from resume.models import Overview
over=Overview.objects.create(text='This is a test overview for this CV')
over.save()

from resume.models import Skillset
from resume.models import Skill
sks=Skillset.objects.create(name='Technical Skills')
s1=Skill.objects.create(name='Data analysis in MATLAB, R, Python',skillset=sks)
s2=Skill.objects.create(name='Experience with relational and NoSQL databases',skillset=sks)
s3=Skill.objects.create(name='UI development in LabView, HTML/Javascript (jQuery, AJAX, D3), LabWindows',skillset=sks)
s1.save()
s2.save()
s3.save()
sks.save()

sks2=Skillset.objects.create(name='Transferable Skills')
s1=Skill.objects.create(name='Troubleshooting: problem solving skills in complex software and hardware problems',skillset=sks2)
s2=Skill.objects.create(name='Strong analytical, multi-tasking and problem solving skills',skillset=sks2)
s1.save()
s2.save()
sks2.save()


from resume.models import Job
j=Job.objects.create(company='MyCompany')
j.start_date=datetime.date(year=2018,month=2,day=19)
j.end_date=datetime.date(year=2018,month=3,day=20)
j.company='Best Co'
j.company_url='https://www.google.com/search?q=best+co'
j.title="CTO"
j.location='Boston, MA'
j.description="Some description of the job which goes here and will be displayed ok you get it"
j.save()

j2=Job.objects.create(company='Booking.com')
j2.start_date=datetime.date(year=2015,month=6,day=19)
j2.end_date=datetime.date(year=2017,month=3,day=20)
j2.company='Booking.com'
j2.company_url='https://www.booking.com'
j2.location='Amsterdam, the Netherlands'
j2.title="Technician"
j2.description="Describe the job here"
j2.save()

from resume.models import JobAccomplishment
acc=JobAccomplishment.objects.create(order=2,job=j)
acc.description="2nd accomplishement"
acc.save()
acc=JobAccomplishment.objects.create(order=3,job=j)
acc.description="my third incomplete accomplishm"
acc.save()
acc=JobAccomplishment.objects.create(order=1,job=j)
acc.description="first accomplishment there"
acc.save()

from resume.models import Achievement
ach1=Achievement.objects.create()
ach1.description="I developed this site. See it on "
ach1.link="https://github.com/aless80/Djangoresume"
ach1.linkname="github"
ach1=Achievement.objects.create()
ach1.save()
ach2=Achievement.objects.create()
ach2.description="Some achievement"
ach2.save()
ach3=Achievement.objects.create()
ach3.description="Some other achievement"
ach3.save()

from resume.models import Education
ed1=Education.objects.create(name='University of Somewhere')
ed1.start_date=datetime.date(year=2010,month=2,day=19)
ed1.end_date=datetime.date(year=2015,month=3,day=1)
ed1.degree="PhD"
ed1.location='Somewhere,FarLand'
ed1.description="Studied spellings"
ed1.save()
ed2=Education.objects.create(name='University of Somewherelse')
ed2.start_date=datetime.date(year=2015,month=4,day=1)
ed2.degree="Hi school"
ed2.location='Boston,MA'
ed2.description="Studied electrodynamics"
ed2.save()

from resume.models import ProgrammingLanguage
pl1=ProgrammingLanguage.objects.create(name='Python',level='Proficient',vote=1)
pl2=ProgrammingLanguage.objects.create(name='Javascript',level='Intermediate',vote=3,order=2)
pl3=ProgrammingLanguage.objects.create(name='C',level='Used in the past',vote=2,order=5)
pl4=ProgrammingLanguage.objects.create(name='Django',level='Daily use',vote=5,order=4)
pl1.save()
pl2.save()
pl3.save()
pl4.save()
```

The available models are: 
Overview
PersonalInfo
Education
Languages
Job
Accomplishment
Skillset
Skill

You can print the available fields for each model using:
```
[f.name for f in Overview._meta.get_fields()]
```# Djangoresume
