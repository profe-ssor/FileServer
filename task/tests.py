from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import WeddingCards, AdmissionForms, BirthdayCards, EngagementCards

# Test case for testing views
class ViewsTestCase(TestCase):
    def setUp(self):
        # Initialize the test client and create test users
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpass123'
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin', 
            email='admin@example.com', 
            password='adminpass123'
        )

    # Test the home view to check if it redirects to login if not authenticated
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirects to login if not authenticated

    # Test the login view to ensure it is accessible
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # Test the register view to ensure it is accessible
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    # Test the admin page view to ensure it is accessible when logged in as an admin
    def test_admin_page_view(self):
        self.client.login(email='admin@example.com', password='adminpass123')
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 200)

    # Test the wedding form view to ensure it is accessible when logged in as a user
    def test_wedding_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('wedding_form'))
        self.assertEqual(response.status_code, 200)

    # Test the admission form view to ensure it is accessible when logged in as a user
    def test_admission_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('admission_form'))
        self.assertEqual(response.status_code, 200)

    # Test the engagement form view to ensure it is accessible when logged in as a user
    def test_engagement_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('engagement_form'))
        self.assertEqual(response.status_code, 200)

    # Test the birthday form view to ensure it is accessible when logged in as a user
    def test_birthday_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('birthday_form'))
        self.assertEqual(response.status_code, 200)

# Test case for testing models
class ModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpass123'
        )

    # Test the creation of a WeddingCards instance
    def test_wedding_card_creation(self):
        card = WeddingCards.objects.create(
            title='Test Wedding Card',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(card, WeddingCards))  # Check if the object is an instance of WeddingCards
        self.assertEqual(card.__str__(), 'Test Wedding Card Test Description')  # Check if the string representation is correct

    # Test the creation of an AdmissionForms instance
    def test_admission_form_creation(self):
        form = AdmissionForms.objects.create(
            title='Test Admission Form',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(form, AdmissionForms))  # Check if the object is an instance of AdmissionForms
        self.assertEqual(form.__str__(), 'Test Admission Form Test Description')  # Check if the string representation is correct

    # Test the creation of a BirthdayCards instance
    def test_birthday_card_creation(self):
        card = BirthdayCards.objects.create(
            title='Test Birthday Card',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(card, BirthdayCards))  # Check if the object is an instance of BirthdayCards
        self.assertEqual(card.__str__(), 'Test Birthday Card Test Description')  # Check if the string representation is correct

    # Test the creation of an EngagementCards instance
    def test_engagement_card_creation(self):
        card = EngagementCards.objects.create(
            title='Test Engagement Card',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(card, EngagementCards))  # Check if the object is an instance of EngagementCards
        self.assertEqual(card.__str__(), 'Test Engagement Card Test Description')  # Check if the string representation is correct
