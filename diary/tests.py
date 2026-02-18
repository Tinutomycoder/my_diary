from django.test import TestCase
from django.contrib.auth.models import User
from .models import DiaryEntry
from django.utils import timezone


class DiaryEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.entry = DiaryEntry.objects.create(
            user=self.user,
            title='Test Entry',
            content='This is a test entry content',
            mood='happy'
        )

    def test_diary_entry_creation(self):
        self.assertEqual(self.entry.title, 'Test Entry')
        self.assertEqual(self.entry.user.username, 'testuser')
        self.assertEqual(self.entry.mood, 'happy')

    def test_diary_entry_str(self):
        expected_str = f"Test Entry - {self.entry.date}"
        self.assertEqual(str(self.entry), expected_str)


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_home_requires_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_home_with_login(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
