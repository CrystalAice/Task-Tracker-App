from django.test import TestCase
from .models import Task

# Create your tests here.
class BlogAppTests(TestCase):
    def setUp(self):

        self.task = Task.objects.create(
            title = 'Watch the 7:30pm news',
            status = 'pending',
            body = 'Check the latest news on stock price movements'

        )

    def test_title_string_representation(self):
        task = Task.objects.create(title = 'Watch the news')
        self.assertEqual(str(task), task.title)
    
    def test_task_details(self):
        self.assertEqual(self.task.title , 'Watch the at 7:30pm news')
        self.assertEqual(self.task.status , 'pending')
        self.assertEqual(self.task.body , 'Check the latest news on stock price movements')
