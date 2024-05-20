from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
