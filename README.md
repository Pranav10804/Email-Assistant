# Email-Assistant
Manage your emails using 'Email Assitant' , a website aimed at streamlining electronic communication and increasing efficiency of your inbox management.
 ## Features
 The website provides two amzing and easy to use features-
 ### Email Classification
 Classify your emails and organize your inbox according to our efficient segregation. The website enables identifies an email as 'Business', 'Entertainment', 'Healthcare' or 'Miscellaneous'. All that is required is the subject of the mail.
 HuggingFace pipeline for a zero shot classification was used to implement such text classification.

 ### Email Summarization
 To save time spent in reading teadious emails, the website has a summarization feature which distills the content of long mails. Give speedy replies to lenghty mails and make deadlines without hardship.
 HuggingFace pipeline for summarization was used to implement text summarization.

 ## How to use
 Run ' py manage.py runserver' command and, using the local host link provided by Django, find the website through '{local_host}/home'
