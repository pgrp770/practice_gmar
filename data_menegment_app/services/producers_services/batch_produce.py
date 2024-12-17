import toolz as t
from typing import List, Callable

@t.curry
def produce_with_chunks(chunks_size: int, data: List, produce: Callable):
    chunk_data = list(t.partition_all(chunks_size, data))
    print(chunk_data)




