def chunking_by(numbers, chunck):
    chunks_list = []

    for i in range(0, len(numbers), chunck):
         # Get a chunk from the list using slicing
        chunk_part = numbers[i:i + chunck]
        chunks_list.append(chunk_part)

    return chunks_list
