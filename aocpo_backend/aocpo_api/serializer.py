#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

class Users(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=11, required=True)
    nickname = serializers.CharField(max_length=20, required=False)
    pwd = serializers.CharField(min_length=6, max_length=16, required=True)

class Task(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=11, required=True)
    scale = serializers.CharField(max_length=5, required=True)
    school = serializers.CharField(max_length=30, required=True)

class DelTask(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=11, required=True)
    school = serializers.CharField(max_length=30, required=True)
    isDel = serializers.IntegerField(required=True)

class GetData(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=11, required=True)
    school = serializers.CharField(max_length=30, required=True)
    offset = serializers.IntegerField(required=True)
    limit = serializers.IntegerField(required=True)
    order = serializers.IntegerField(required=True)
    classify = serializers.IntegerField(required=False)
    sentiment = serializers.IntegerField(required=False)
    date_start = serializers.CharField(required=False)
    date_end = serializers.CharField(required=False)

class GetPostsAnalysisData(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=11, required=True)
    school = serializers.CharField(max_length=30, required=True)
    date_start = serializers.IntegerField(required=False)
    date_end = serializers.IntegerField(required=False)
    days = serializers.IntegerField(required=False)