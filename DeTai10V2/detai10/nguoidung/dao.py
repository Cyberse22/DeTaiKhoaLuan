from nguoidung.models import NguoiDung
from django.db.models import Count


def load_users(params={}):
    q = NguoiDung.objects.filter(active=True)

    kw = params.get('kw')
    if kw:
        q = q.filter(name__icontains=kw)

    user_id = params.get('user_id')
    if user_id:
        q = q.filter(UID=user_id)

    return q


def count_users_by_user_id():
    return NguoiDung.objects.annonate(count=Count('user_id'))\
                  .values('UID', 'name', 'count').order_by('-count')