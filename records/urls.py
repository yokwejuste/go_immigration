from django.urls import path

from records.views import register, login_go_user, \
    logout_go_user, choices, SearchResult, dashboard, \
    profile, records, send_files_1, preview, send_files_2, send_files_3  # ,h404

urlpatterns = [
    path('', register, name='register'),
    path('register', register, name='register'),
    path('login', login_go_user, name='login'),
    path('logout', logout_go_user, name='logout'),
    path('choices', choices, name='choices'),
    path('search', SearchResult.as_view(), name='search'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('records', records, name='records'),
    path('preview', preview, name='preview'),
    # path('query_life_is_good', h404, name='h404'),
    # url(r'^$', h404, name='page_not_found'),
    path('upload_s', send_files_1, name='upload_s'),
    path('upload_t', send_files_2, name='upload_t'),
    path('upload_v', send_files_3, name='upload_v'),
]

handlers404 = 'records.views.handlers404'
