# //Backend\Students\views.py
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import make_password


from .models import StudentDetails

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            # Fetch user data from your database (example)
            # Assuming you have a `Student` model with `email` and `password` fields
            from .models import Student
            user = Student.objects.filter(email=email).first()

            if user and check_password(password, user.password):
                return JsonResponse({
                    'status': 'success',
                    'message': 'Login successful',
                    'data': {
                        'email': user.email,
                        'full_name': user.full_name,
                    }
                })
            return JsonResponse({'status': 'error', 'message': 'Invalid email or password'}, status=401)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            full_name = data.get('full_name')
            email = data.get('email')
            password = data.get('password')
            date_of_birth = data.get('date_of_birth')
            identity_proof_type = data.get('identity_proof_type')
            identity_proof_number = data.get('identity_proof_number')
            course = data.get('course')
            mobile_number = data.get('mobile_number')
            print("1")
            # Check if email already exists
            if StudentDetails.objects.filter(email=email).exists():
                print("2")
                return JsonResponse({'status': 'error', 'message': 'Email already registered'}, status=400)
            print("3")
            # Save the student
            student = StudentDetails(
                full_name=full_name,
                email=email,
                password=make_password(password),
                date_of_birth=date_of_birth,
                identity_proof_type=identity_proof_type,
                identity_proof_number=identity_proof_number,
                course=course,
                mobile_number=mobile_number
            )
            
            print("4")
        
            print("Student data:", student)  # Add logging here
            student.save()

            return JsonResponse({'status': 'success', 'message': 'Registration successful'})

        except Exception as e:
            print("Error during registration:", str(e))  # Add logging here
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
