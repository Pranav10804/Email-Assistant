from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ClassifyForm, SummariseForm
from transformers import pipeline
classifier = pipeline("zero-shot-classification")
summariser= pipeline("summarization")

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
# Create your views here.

def submit(request):
  context ={}
  context['form']= ClassifyForm()
  return render(request, "submit.html", context)

def classify(request):
  if request.method == 'POST':
    form =ClassifyForm(request.POST, request.FILES)
    if form.is_valid():
      subject_line = form.cleaned_data['subject']
      candidate_labels = ["Business", "Healthcare", "Entertainment", "Miscellaneous"]
      result = classifier(subject_line, candidate_labels)
      classification = result['labels'][0]
    else:
      form=ClassifyForm()
  return render(request, 'classify_email.html', {'form': form, 'classification': classification})

def submit1(request):
  context={}
  context['form']=SummariseForm()
  return render(request, "submit1.html", context)

def summarise(request):
  if request.method == 'POST':
    form =SummariseForm(request.POST, request.FILES)
    if form.is_valid():
      content = form.cleaned_data['content']
      result = summariser(content)
      summary = result[0]['summary_text']
    else:
      form=SummariseForm()
  return render(request, 'summarise_email.html', {'form': form, 'summary': summary})
