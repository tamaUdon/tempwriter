import functools
import asyncio

from asyncio import events
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, TypeVar
from printer import controller as printer

T = TypeVar("T")

# async非対応のescpos対策. ThreadPoolExecutorをasyncで包む
# ref. https://www.rhoboro.com/2021/06/13/to_subthread_to_subprocess.html
async def to_subthread(func: Callable[..., T], /, *args: Any, **kwargs: Any) -> T:
    """I/Oバウンドなブロッキング処理の関数をコルーチンに変換して実行"""
    loop = events.get_running_loop()
    executor = ThreadPoolExecutor(max_workers=1)
    func_call = functools.partial(func, *args, **kwargs)
    return await loop.run_in_executor(executor, func_call)


def main():
    printer.init_printer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(to_subthread(printer.output_and_cut, "apple🍎orange🍊bananna🍌"))

if __name__ == "__main__":
    main()
