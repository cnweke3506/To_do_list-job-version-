# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:47:54 2024

@author: chuka
"""
import sys
    
def view_job(jobs):
    if not jobs:
        print("\nYour job list is empty")
    else:
        print("\nYour jobs list")
        for i, job in enumerate(jobs, start =1):
            print(f'{i}. {job}')
        
    
def display_message():
    print("\nWelcome to my dream job listing")
    print("1. To add to my dream job")
    print("2. To view my dream job")
    print("3. To delete from my dream job")
    print("4. To exit the application")
    
def commot_job(jobs):
    if not jobs:
        print("\nYour job list is empty! there is nothing to delete")
        return
    view_job(jobs)
    try:
        job_selection = int(input("\nEnter job number you want to delete: "))
        if 1 <= job_selection <= len(jobs):
            job_number = jobs.pop(job_selection -1)
            print(f'{job_number} succesffuly deleted')
        else: 
            print("invalid job number, try again")
            
    except ValueError:
        print("invalid selection, enter a valid number")

def add_job(jobs):
    job = input("\nEnter your dream job: ")
    jobs.append(job)
    print(f"Dream job {job} has successfully been added")
    
    
def main():
    jobs = []
    
    while True:
        display_message()
        print()
        
        choice = (input("\nEnter a number from options: "))
        
        if choice == '1':
            add_job(jobs)
        elif choice == '2':
            view_job(jobs)
        elif choice == '3':
            commot_job(jobs)
        elif choice == '4':
            print("\nExciting application! Goodbye")
            sys.exit()
            
        else:
                print("\nInvalid selection, Try again")
                
    
    
if __name__=='__main__':
    main()
        