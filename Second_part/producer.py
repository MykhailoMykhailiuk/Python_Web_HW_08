from faker import Faker
from mongoengine import connect
from model import Contacts
import pika

URI = "mongodb+srv://misamihajluk1:A03LBdqNq5xiqcmw@contactsmongo.rvxofnn.mongodb.net/?retryWrites=true&w=majority&appName=ContactsMongo"

connect(host=URI)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        credentials=credentials
    )
)
chanel = connection.channel()
chanel.queue_declare(queue='email_queue')

Faker.seed(1)
fake = Faker()


def main():
    for _ in range(10):
        name = fake.name()
        email = fake.email()
        phone = '+380'
        phone += str(fake.random_number(digits=9, fix_len=True))
        adress = fake.address()

        contact = Contacts(
            full_name=name,
            email=email,
            phone=phone,
            address=adress
        ).save()

        chanel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id).encode())
        print(f'[x] Sent {contact.id}')

    connection.close()


if __name__ == '__main__':
    main()