from django_assets import Bundle, register

js = Bundle(
    'vendor/jquery/jquery.min.js',
    'vendor/prismjs/prism.js',
    'js/main.js',
    filters='jsmin',
    output='gen/packed.js')

css = Bundle(
    'vendor/prismjs/prism.css',
    'css/main.css',
    filters='cssmin',
    output='gen/main.css')

register('js_all', js)
register('css_all', css)
