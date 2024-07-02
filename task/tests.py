from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import WeddingCards, AdmissionForms, BirthdayCards, EngagementCards

class ViewsTestCase(TestCase):
    def setUp(self):
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

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirects to login if not authenticated

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_admin_page_view(self):
        self.client.login(email='admin@example.com', password='adminpass123')
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 200)

    def test_wedding_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('wedding_form'))
        self.assertEqual(response.status_code, 200)

    def test_admission_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('admission_form'))
        self.assertEqual(response.status_code, 200)

    def test_engagement_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('engagement_form'))
        self.assertEqual(response.status_code, 200)

    def test_birthday_form_view(self):
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('birthday_form'))
        self.assertEqual(response.status_code, 200)

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpass123'
        )

    def test_wedding_card_creation(self):
        card = WeddingCards.objects.create(
            title='Test Wedding Card',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(card, WeddingCards))
        self.assertEqual(card.__str__(), 'Test Wedding Card Test Description')

    def test_admission_form_creation(self):
        form = AdmissionForms.objects.create(
            title='Test Admission Form',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(form, AdmissionForms))
        self.assertEqual(form.__str__(), 'Test Admission Form Test Description')

    def test_birthday_card_creation(self):
        card = BirthdayCards.objects.create(
            title='Test Birthday Card',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(card, BirthdayCards))
        self.assertEqual(card.__str__(), 'Test Birthday Card Test Description')

    def test_engagement_card_creation(self):
        card = EngagementCards.objects.create(
            title='Test Engagement Card',
            description='Test Description',
            email=self.user
        )
        self.assertTrue(isinstance(card, EngagementCards))
        self.assertEqual(card.__str__(), 'Test Engagement Card Test Description')