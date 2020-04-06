from rest_framework.response import Response
from rest_framework.views import APIView
from .BaseResponse import BaseResponse
from .senta_model_release.predictor import SentaPre
from .content_classification_model_release.predictor import ConPre

#调用模型
class CfyAndSen(APIView):
    def get(self, response):
        data = response.query_params.get('data')
        sen_predictor = SentaPre(data=data)
        con_predictor = ConPre(data=data)
        con_pre = con_predictor.predict()
        sen_pre = sen_predictor.predict()
        res = BaseResponse()
        res.status = 1000
        res.msg = '成功'
        res.data = {
            'sentiment': sen_pre,
            'classify': con_pre
        }
        return Response(res.get_dict)