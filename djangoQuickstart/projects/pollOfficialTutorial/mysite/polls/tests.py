import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question


#HELPER FUNCTIONS

#generate and persist a question with given text and timedelta from today
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date=time)



#the queryset for index should contain only previous questions or display message if there
#are no questions

class QuestionDetailViewTests(TestCase):

    #make sure that requesting detail for a future question yields 404 response
    def test_past_question(self):
        past_question = create_question(question_text="question of the past!", days = -1)
        url = reverse("polls:detail", args=[past_question.id])
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    #make sure that when requesting detail for past question, response contains past question's text
    def test_future_question(self):
        future_question = create_question(question_text="future question", days = 1)
        url = reverse("polls:detail", args=[future_question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        question = create_question(question_text="past question", days=-30)
        response = self.client.get(reverse('polls:index')) 
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
        
    def test_future_question(self):
        question = create_question(question_text="future question", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], []) 

    def test_future_question_and_past_question(self):
        create_question(question_text="future question", days = 30)
        past_question = create_question(question_text="past question", days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question]) 
    
    def test_two_past_questions(self):
        past_question1 = create_question(question_text="future question", days = -30)
        past_question2 = create_question(question_text="past question", days = -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question2, past_question1]) 

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


