from django.shortcuts import render

# Create your views here.
service_context = {
    'service': [
        {'name': 'Web development (frontend, backend, full-stack)','price':'#500,000'},
        {'name':'Mobile app development (iOS, Android)','price':'#1,000,000'},
        {'name': 'WordPress development','price': '#1,000,000'},
        {'name': 'E-commerce site setup (Shopify, WooCommerce)','price': '#1,000,000'},
        {'name': 'Data analysis','price': '#1,000,000'},
        ]
}

 
testimonials_context = {
      'testimonials': [
        {'name': 'winnie.', 'text': "Fast, professional, and exactly what we needed!"},
        {'name': 'Akeem.', 'text': "Delivered high quality work ahead of schedule."},
        {'name': 'Niko.', 'text': "Reliable and super easy to work with."},
        {'name': 'Tobi.', 'text': "Understood the vision and nailed it!"},
        {'name': 'David K.', 'text': "The very best,Would definitely hire again!"},
    ]
}

def service(requests):
    return render(requests,'freelance/service.html',service_context)

def testimonials(requests):
    return render(requests,'freelance/testimonials.html',testimonials_context)

def case_study(requests):
    return render(requests,'freelance/case_study.html')

def blog(requests):
    return render(requests,'freelance/blog.html')

def pricing(requests):
    return render(requests,'freelance/pricing.html',service_context)


