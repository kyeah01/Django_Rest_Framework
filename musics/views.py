from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music
from .serializers import MusicSerializer

# Create your views here.

# response를 통해 serializer를 반환
# serializer - 특정한 딕셔너리 혹은 쿼리셋등의 파이썬 형식 데이터 타입을 반환하도록 해줌.

# musics는 쿼리셋, 일종의 리스트.
# 응답하려고 하는 것은 제이슨.
# 따라서 뮤직 시리얼라이져가 하는 일은, 리스트를 하나하나씩 제이슨 타입으로 바꿔주는 일.
# 응답하는 함수는 response. 결과로 보내줄 데이터는 .data로 가져옴.

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def music_detail(request, music_pk):
    musics = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(musics)
    return Response(serializer.data)