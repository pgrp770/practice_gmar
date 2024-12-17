import toolz as t
from typing import List, Callable

def produce_chunks(data: List, produce: Callable, chunks_size: int):
    [produce(item) for item in list(t.partition_all(chunks_size, data))]
