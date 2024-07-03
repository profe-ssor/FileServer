from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout # Functions for user authentication, logging in, and logging out.
from django.contrib import messages # Enables message passing between views, often used for displaying notifications to users.
from . forms import RegistrationForm, AdmissionForm, WeddingForm, EngagementForm, BirthdayForm
from django.contrib.auth.decorators import login_required, user_passes_test # Decorators to restrict access to views based on user authentication status or custom tests.
from .models import WeddingCards, AdmissionForms, BirthdayCards, EngagementCards, MyUser
from django.http import Http404, HttpResponse, FileResponse # Used to create HTTP responses directly.
from django.shortcuts import get_object_or_404 # Utility to fetch an object or return a 404 error if it doesn’t exist.
from .filters import WeddingCardFilter, EngagementCardFilter, BirthdayCardFilter, AdmissionCardFilter
from django.core.mail import EmailMessage # Facilitates sending emails.
from django.conf import settings
import mimetypes# Standard Python library to handle MIME types.  Used to guess the MIME type of a file based on its filename or URL



# Create your views here.

# Accounts Handling
def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegistrationForm()
        context = {'form':form}
        if request.method=='POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Successfully Created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'authentication/register.html', context )

def loginpage(request):
    if request.method=="POST":
        email= request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Wrong Spelt or email or Password')
            return redirect('login')
    else:       
        return render(request, "authentication/login.html")
    
def logoutUser(request):
    logout(request)
    return redirect('login')
# EndsAccouts Handling

@login_required(login_url='login')  
def Customer_page(request):
    wedding_cards = WeddingCards.objects.all()
    birthday_cards = BirthdayCards.objects.all()
    admission_cards = AdmissionForms.objects.all()
 
    context  = {
        'wedding_cards':wedding_cards, 
        'birthday_cards': birthday_cards,
        'admission_cards': admission_cards,
    }
    return render(request, 'task/customer_page.html', context)

def is_admin(user):
    return user.is_authenticated and user.is_staff  # or user.is_superuser based on your needs

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def admin_page(request):
    wedding_cards = WeddingCards.objects.all()
    engagement_cards = EngagementCards.objects.all()
    birthday_cards = BirthdayCards.objects.all()
    admission_cards = AdmissionForms.objects.all()

    context = {
        'wedding_cards_count': wedding_cards.count(),
        'engagement_cards_count': engagement_cards.count(),
        'birthday_cards_count': birthday_cards.count(),
        'admission_cards_count': admission_cards.count(),
        'wedding_cards_downloaded': sum(card.download_count for card in wedding_cards),
        'engagement_cards_downloaded': sum(card.download_count for card in engagement_cards),
        'birthday_cards_downloaded': sum(card.download_count for card in birthday_cards),
        'admission_cards_downloaded': sum(card.download_count for card in admission_cards),
        'wedding_cards_emailed': sum(card.email_count for card in wedding_cards),
        'engagement_cards_emailed': sum(card.email_count for card in engagement_cards),
        'birthday_cards_emailed': sum(card.email_count for card in birthday_cards),
        'admission_cards_emailed': sum(card.email_count for card in admission_cards),
    }

    return render(request, 'task/admin_page.html', context)


# Available Cards Pages

def wedding_cards(request):
    wedd_cards = WeddingCards.objects.all()
    card_filter = WeddingCardFilter(request.GET, queryset=wedd_cards)
    wedd_cards = card_filter.qs
    context = {
        'wedd_cards': wedd_cards,
        'card_filter': card_filter
    }
    return render(request, 'task/wedding/wedding_cards.html', context)

def admission_cards(request):
    admission_cards = AdmissionForms.objects.all()
    # Filtering based on search input
    card_filter = AdmissionCardFilter(request.GET, queryset=admission_cards)
    admission_cards = card_filter.qs

    context = {
        'admission_cards': admission_cards,
        'card_filter': card_filter
    }
    return render(request, 'task/admission/admission_cards.html', context)

def engagement_cards(request):
    engagement_cards = EngagementCards.objects.all()
    # Filtering based on search input
    card_filter = EngagementCardFilter(request.GET, queryset=engagement_cards)
    engagement_cards = card_filter.qs

    context = {
        'engagement_cards': engagement_cards,
        'card_filter': card_filter
    }
    return render(request, 'task/engagement/engagement_cards.html', context)

def birthday_cards(request):
    birthday_cards = BirthdayCards.objects.all()
    # Filtering based on search input
    card_filter = BirthdayCardFilter(request.GET, queryset=birthday_cards)
    birthday_cards = card_filter.qs

    context = {
        'birthday_cards': birthday_cards,
        'card_filter': card_filter
    }
    return render(request, 'task/birthday/birthday_cards.html', context)

# Available Cards Pages Ends

# Available Forms View


def wedding_form(request):
    form = WeddingForm()
    users = MyUser.objects.all()
    if request.method=='POST':
        form = WeddingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WeddingForm()
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'task/wedding/wedding_forms.html', context)



def admission_form(request):
    form = AdmissionForm()
    users = MyUser.objects.all()
    if request.method=='POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdmissionForm()
    context = {
        'form': form,
        'users': users
    }
    
    return render(request, 'task/admission/admission_form.html', context)

def engagement_form(request):
    form = EngagementForm()
    users = MyUser.objects.all()
    if request.method=='POST':
        form = EngagementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EngagementForm()
    context = {
        'form': form,
        'users': users
    }
   
    return render(request, 'task/engagement/engagement_form.html', context )

def birthday_form(request):
    form = BirthdayForm()
    users = MyUser.objects.all()
    if request.method=='POST':
        form =  BirthdayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =  BirthdayForm()
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'task/birthday/birthday_form.html', context  )

# Available Forms View Ends

# Feed Page View Starts

def feed_page(request):
    # Get all files
    wedd_cards = WeddingCards.objects.all()
    birthday_cards = BirthdayCards.objects.all()
    admission_cards = AdmissionForms.objects.all()
    engagement_cards = EngagementCards.objects.all()

    # Filtering based on search input
    wedding_filter = WeddingCardFilter(request.GET, queryset=wedd_cards)
    wedd_cards = wedding_filter.qs

    engagement_filter = EngagementCardFilter(request.GET, queryset=engagement_cards)
    engagement_cards = engagement_filter.qs

    birthday_filter = BirthdayCardFilter(request.GET, queryset=birthday_cards)
    birthday_cards = birthday_filter.qs

    admission_filter = AdmissionCardFilter(request.GET, queryset=admission_cards)
    admission_cards = admission_filter.qs

    context = {
        'wedd_cards': wedd_cards,
        'engagement_cards': engagement_cards,
        'birthday_cards': birthday_cards,
        'admission_cards': admission_cards,
        'wedding_filter': wedding_filter,
        'engagement_filter': engagement_filter,
        'birthday_filter': birthday_filter,
        'admission_filter': admission_filter,
    }

    return render(request, 'task/feed_page.html', context)

# Feed Page View Ends

# All the Available Forms Starts

def form_link(request):
    return render(request, 'task/form_links.html')

# All the Available Forms Ends

#CRUD Operations Starts

def crud_page(request):
        # Get all files
    wedd_cards = WeddingCards.objects.all()
    birthday_cards = BirthdayCards.objects.all()
    admission_cards = AdmissionForms.objects.all()
    engagement_cards = EngagementCards.objects.all()

    context = {
        'wedd_cards': wedd_cards,
        'engagement_cards': engagement_cards,
        'birthday_cards': birthday_cards,
        'admission_cards': admission_cards,
    }

    return render(request, 'task/check_page.html', context)


# Update Starts


def update_form(request, pk, form_class, template_name):
    users = MyUser.objects.all()
    instance = get_object_or_404(form_class.Meta.model, id=pk)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = form_class(instance=instance)
    context = {
        'users': users,
        'form': form,
        'instance': instance
    }
    return render(request, template_name, context)

def update_wedding(request, pk):
    return update_form(request, pk, WeddingForm, 'task/wedding/wedding_form_update.html')

def update_birthday(request, pk):
    return update_form(request, pk, BirthdayForm, 'task/birthday/birthday_form_update.html')

def update_admission(request, pk):
    return update_form(request, pk, AdmissionForm, 'task/admission/admission_form_update.html')

def update_engagement(request, pk):
    return update_form(request, pk, EngagementForm, 'task/engagement/engagement_form_update.html')

# Update Ends

# Delete Starts

@login_required
def delete_file(request, file_type, file_id):
    if file_type == 'wedding':
        file = get_object_or_404(WeddingCards, id=file_id)
    elif file_type == 'birthday':
        file = get_object_or_404(BirthdayCards, id=file_id)
    elif file_type == 'admission':
        file = get_object_or_404(AdmissionForms, id=file_id)
    elif file_type == 'engagement':
        file = get_object_or_404(EngagementCards, id=file_id)
    else:
        messages.error(request, 'Invalid file type')
        return redirect('home')

    if request.method == 'POST':
        file.delete()
        messages.success(request, f'{file_type.capitalize()} card deleted successfully.')
        return redirect('home')

    return render(request, 'task/CRUD/delete.html', {'file': file})

# Delete Ends

# CRUD OPERATIONS ENDS

# Downloads Functions

def download_file(request, file_id, file_type):
    if file_type == 'wedding':
        file = get_object_or_404(WeddingCards, id=file_id)
    if file_type == 'engagement':
        file = get_object_or_404(EngagementCards, id=file_id)
    elif file_type == 'birthday':
        file = get_object_or_404(BirthdayCards, id=file_id)
    elif file_type == 'admission':
        file = get_object_or_404(AdmissionForms, id=file_id)

    file.download_count += 1
    file.save()

    response = HttpResponse(file.upload_card, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.upload_card.name}"'
    
    return response

# Email Function

def send_file(request, file_id, file_type):
    if request.method == 'POST':
        recipient_email = request.POST['recipient_email']

        if file_type == 'wedding':
            file = get_object_or_404(WeddingCards, id=file_id)
        elif file_type == 'birthday':
            file = get_object_or_404(BirthdayCards, id=file_id)
        elif file_type == 'admission':
            file = get_object_or_404(AdmissionForms, id=file_id)
        elif file_type == 'engagement':
            file = get_object_or_404(EngagementCards, id=file_id)
        else:
            return HttpResponse("Invalid file type", status=400)

        file_path = file.upload_card.path
        file_name = file.upload_card.name
        file_mime_type, _ = mimetypes.guess_type(file_path)

        email = EmailMessage(
            subject=f"Here's your {file_type} card",
            body=f"Please find attached the {file_type} card titled '{file.title}'.",
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient_email],
        )
        email.attach(file_name, file.upload_card.read(), file_mime_type or 'application/octet-stream')
        email.send()

        # Increment email count
        file.email_count += 1
        file.save()

        messages.success(request, 'File sent successfully to ' + recipient_email)
        return redirect('home')

    return HttpResponse("Invalid request method", status=400)

# view Cards Controls
def card_detail(request, card_type, card_id):
    if card_type == 'wedding':
        card = get_object_or_404(WeddingCards, id=card_id)
    elif card_type == 'birthday':
        card = get_object_or_404(BirthdayCards, id=card_id)
    elif card_type == 'admission':
        card = get_object_or_404(AdmissionForms, id=card_id)
    elif card_type == 'engagement':
        card = get_object_or_404(EngagementCards, id=card_id)
    else:
        raise Http404("Card type not found")

    return render(request, 'task/card_detail.html', {'card': card, 'card_type': card_type})


def view_file(request, file_type, file_id):
    if file_type == 'wedding':
        file = get_object_or_404(WeddingCards, id=file_id)
    elif file_type == 'birthday':
        file = get_object_or_404(BirthdayCards, id=file_id)
    elif file_type == 'admission':
        file = get_object_or_404(AdmissionForms, id=file_id)
    elif file_type == 'engagement':
        file = get_object_or_404(EngagementCards, id=file_id)
    else:
        return HttpResponse("Invalid card type", status=400)

    file_path = file.upload_card.path
    file_mime_type, _ = mimetypes.guess_type(file_path)

    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=file_mime_type or "application/octet-stream")
        response['Content-Disposition'] = f'inline; filename={file.upload_card.name}'
        return response
