from django.test import TestCase
from apps.workers.models import Brigade, Worker


class WorkerTestCase(TestCase):

    def setUp(self):
        self.brigade = Brigade.objects.create(
            number=1
        )
        self.brigade_two = Brigade.objects.create(
            number=2
        )

        self.worker = Worker.objects.create(
            full_name='Ivan Ivanov',
            salary=10,
            specialization='test'
        )
        self.worker.brigade_number.set([self.brigade])

        self.worker_two = Worker.objects.create(
            full_name='Denis Ivanov',
            salary=10,
            specialization='test2'
        )
        self.worker_two.brigade_number.set([self.brigade_two])

        self.worker_three = Worker.objects.create(
            full_name='Oleg Ivanov',
            salary=10,
            specialization='test3'
        )
        self.worker_three.brigade_number.set([self.brigade_two, self.brigade])

    def test_worker(self):
        response = self.client.get(f'/api/v1/worker/{self.worker.id}/')
        self.assertEqual(response.data['full_name'], self.worker.full_name)

    def test_team(self):
        response = self.client.get(f'/api/v1/team/{self.brigade_two.id}/WorkerList/')
        self.assertEqual(len(response.data), 2)
