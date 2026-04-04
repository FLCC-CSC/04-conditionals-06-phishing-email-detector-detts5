# FILE NAME - phishing_email_detector.py

# NAME: Dan Dettman
# DATE: 4/1/2026
# BRIEF DESCRIPTION: This program analyzes an email subject line
# to detect possible phishing attempts based on common red flags. 

subject = input("Enter the email subject line: ")
subject = subject.lower()

if "urgent" in subject or "immediate action required" in subject:
    print("HIGH RISK: Possible phishing attempt.")
elif "win" in subject or "free" in subject:
    print("MEDIUM RISK: Suspicious offer detected.")
elif "password reset" in subject:
    print("LOW RISK: Verify legitimacy with sender.")
else:
    print("No phishing indicators detected.")















    







#1. Was using `in` difficult or was it natural? Difficult















#Please gauge your utilization of AI on the following spectrum. Place an "X" in front
#of the appropriate response. Only choose one of the following:

#[ ] I did not use AI at all for this lab.
#[X] I wrote the initial draft of the software but had AI help me make it better.
#[ ] I fed the lab description to AI and had it generate a response but I modified it.
#[ ] AI created the entire program for me.



#It is critical in this class that you understand the concepts as we explore them because
#those concepts are required understanding for entry level programming. Reliance on resources
#like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
#may impede your understanding. Please rate how well you understand the concepts in this lab: 

#[ ] I understand very little about this lab.
#[X] I am about 50/50 on this lab; I get parts of it but not the whole picture.
#[ ] I pretty much get it.
#[ ] I'm solid. Totally got it.


