def handle_upload_File(f):
    with open('documents/' + f.name, 'wb') as destination:
        for chunks in f.chunks:
            destination.write(chunks)
