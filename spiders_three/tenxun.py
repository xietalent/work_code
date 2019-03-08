
import requests
import re
import pytesseract
import pymysql
import redis
import urllib3
import urllib
import time
import random

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from lxml import etree
from urllib import request,response
from PIL import Image
from aip import AipOcr