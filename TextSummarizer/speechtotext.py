from __future__ import print_function
import time
import boto3
import urllib.request
import json
def obtainTranscript(audiofile,name):
	transcribe = boto3.client('transcribe')
	print(transcribe)
	job_name = name
	job_uri = audiofile
	print("test1")
	transcribe.start_transcription_job(
		TranscriptionJobName=job_name,
		Media={'MediaFileUri': job_uri},
		MediaFormat='wav',
		LanguageCode='en-US'
	)
	print("test2")
	while True:
		print("in while")
		status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
		if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
			break
		print("Not ready yet...")
		time.sleep(5)
	print(status)

	fileUrl = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
	fileName = name+".json"
	urllib.request.urlretrieve(fileUrl,fileName)
	data = json.load(open(fileName))
	transcript = (data["results"]["transcripts"][0]["transcript"]).split(".")
    inputPath = 'resources/InputFiles/'
    outputFilePath = inputFilePath = join(getcwd(), inputPath)
	transcribeFile = name+ outputFilePath +"Transcribe.txt"
	file = open(transcribeFile,"w")
	for line in transcript:
		file.write(line)
		file.write("\n")
	file.close()
url = input("enter the lecture clip url")
print(url)
jobName = input("enter job name") 
obtainTranscript(url,jobName)

