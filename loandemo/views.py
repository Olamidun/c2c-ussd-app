from datetime import datetime
from .models import LoanModel, UssdUser
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# This is to bypass the {% csrf_token %} security feature django's put in place for POST requests
@csrf_exempt
def ussd_user(request):
    if request.method == 'POST':

        session_id = request.POST.get('sessionId', None)
        service_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")
        text_list = text.split('*')
        print(text_list)

        try:
            response = ""
            user = UssdUser.objects.get(phone_number=phone_number)
            print(user)
            if text == '':
                response  = "CON What is your transaction pin\n"

            elif len(text_list) == 1 and text_list[0] == user.transaction_pin:
                response = "CON 1. Press 1 to repay your loan"
            
            elif len(text_list) == 2 and text_list[1] == '1':
                loan_model = LoanModel.objects.get(user=user)
                loan_model.paid = True
                loan_model.save()
                response = "END Your loan has been repaid"

            return HttpResponse(response)
        except UssdUser.DoesNotExist:
            # This is so we can access each input we are collecting from the user
            response = ""
            if text == '':
                
                response  = "CON What do you want to do \n"
                response += "1. Create account\n"
                response += "2. Check loan services"
        
            elif len(text_list) == 1:
                response = "CON Please enter your full name\n"

            elif len(text_list) == 2:
                response = "CON Please enter your phone number\n"
            
            elif len(text_list) == 3:
                response = "CON Enter your date of birth in this format (dd-mm-yy)"
            elif len(text_list) == 4:
                response = "CON Enter a four digit pin"
            elif len(text_list) == 5:
                if len(text_list[4]) > 4 or len(text_list[4]) < 4:
                    response = "END Your pin must have exactly 4 characters"
                else:
                    # Saves user that registers on the USSD application to the database
                    UssdUser.objects.create(name=text_list[1], phone_number=text_list[2], date_of_birth=datetime.strptime(text_list[3], '%d-%m-%Y'), transaction_pin=text_list[4])

                    response = "CON Your transaction pin has been set successfully. Choose the action you want to perform\n"
                    response += "1. Apply for loan\n"
                    response += "2. Repay Loan\n"

            elif len(text_list) == 6 and text_list[5] == '1':
                response = "CON Choose payment plan and enter the amount you want to borrow in this format: plan, amount. e.g 1, 50000\n"
                response += "1. Pay back weekly\n"
                response += "2. Pay back monthly\n"

            elif text_list[5] == '1' or text_list[5] == '2':
                # Get a user trying to apply for loan so we can assign it to the user attribute in LoanModel  
                user = UssdUser.objects.get(phone_number=text_list[2], name=text_list[1])

                loan_plan_and_amount = text_list[6].split(', ')
                print(loan_plan_and_amount)
                LoanModel.objects.create(amount=loan_plan_and_amount[1], plan=loan_plan_and_amount[0], user=user)
                response = "END Your loan application has been successfully received"

            return HttpResponse(response)
