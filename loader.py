#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    
    try:
        from django.contrib.auth.models import User
        from blog.models import Category, Tag, Post
        from faker import Faker
        import random
        
        
        fake = Faker()
        
        def create_users(max = 5):
            for _ in range(max):
                User.objects.create(username=fake.user_name(),
                                    first_name=fake.first_name() ,
                                    last_name=fake.last_name() ,
                                    email=fake.email())
        
        def create_categories(max = 5):
            for _ in range(max):
                Category.objects.create(
                                    name=fake.word(),
                                    description=fake.sentence() ,
                                        )   
        def create_tags(max = 5):
            for _ in range(max):
                Tag.objects.create(
                                    name=fake.word(),
                                    description=fake.sentence() ,
                                        )   
        def create_posts(max = 50):
            users = list(User.objects.all())
            categories = list(Category.objects.all())
            tags = list(Tag.objects.all())
            for _ in range(max):
                post = Post.objects.create(
                                            title=fake.sentence(),
                                            #slug=fake.slug() ,
                                            content=fake.paragraph(nb_sentences=random.randint(60,100)),
                                            author=fake.random.choice(users),
                                            category=fake.random.choice(categories),
                                            is_published=fake.boolean(),
                                            created_at=fake.date_time_this_decade(),
                                            updated_at=fake.date_time_this_year(),
                                            ) 
            post.tags.set(random.sample(tags,random.randint (1, 5)))
    
        create_users(20)
        create_tags(7)
        create_categories(10)
        # create_posts(100)
        
        
    except Exception as err:
       print(err)


if __name__ == '__main__':
    main()
