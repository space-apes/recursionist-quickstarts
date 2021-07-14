import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


#Helper functions
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date=time)


# Create your tests here.

class QuestionIndexViewTests(TestCase):
    


class QuestionModelTests(TestCase):
    #case for distant past should yield False
    def test_was_published_recently_with_past_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date = time)
        self.assertIs(past_question.was_published_recently(), False)

    #case for published within a day should yield True
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)

    #case for posted in the future should yield False
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)


