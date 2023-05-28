import json
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.generic import View
from recipes.models import *
from recipes.forms import *


class RecipeReviewCreateView(LoginRequiredMixin, View):
    model = RecipeReview
    template_name = 'recipes/review_detail.html'
    pk_url_kwarg = 'review_pk'


    def post(self, request, *args, **kwargs):
        jsonObject = json.loads(request.body)
        recipe_pk = jsonObject.get('pk')
        content = jsonObject.get('content')
        review = RecipeReview.objects.create(
            recipe = Recipe.objects.get(pk=recipe_pk),
            user = request.user,
            content = content
        )
        review.save()

        context = {
            'user': review.user.pk,
            'content': review.content,
            'created_at': review.created_at,
            'updated_at': review.updated_at
        }
        return JsonResponse(context)


class RecipeReviewUpdateView(LoginRequiredMixin, View):
    model = RecipeReview
    template_name = 'recipes/recipe_detail.html'
    pk_url_kwarg = 'review_pk'


    def post(self, request, *args, **kwargs):
        jsonObject = json.loads(request.body)
        review_pk = jsonObject.get('pk')
        content = jsonObject.get('content')
        review = RecipeReview.objects.get(pk=review_pk)

        if review.user == request.user:
            if review is not None:
                review.content=jsonObject.get('content')
                review.save()
                context = {
                    'content': content
                }
                return JsonResponse(context)
            return JsonResponse({'result': 'error!'}, status=400)
        else:
            raise PermissionDenied()


class RecipeReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    model = RecipeReview
    template_name = 'recipes/recipe_detail.html'
    pk_url_kwarg = 'review_pk'


    def test_func(self):
        review = RecipeReview.objects.get(pk=self.kwargs['review_pk'])
        return self.request.user == review.user
    

    def post(self, request, *args, **kwargs):
        jsonObject = json.loads(request.body)
        review = RecipeReview.objects.get(pk=jsonObject.get('review_pk'))
        if review is not None:
            review.delete()
            return JsonResponse({'result': 'success'})
        return JsonResponse({'result': 'fail'})