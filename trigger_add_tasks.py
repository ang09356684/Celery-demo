from tasks import add, add_with_bind, add_with_custom_task

add_result = add.apply_async(args=(1, 2), queue='demo')
print(f'add result: {add_result}')

bind_result = add_with_bind.apply_async(args=(1, 2), queue='demo')
print(f'bind result: {bind_result}')

custom_task_result = add_with_custom_task.apply_async(args=(1, 2), queue='demo')
print(f'custom task result: {custom_task_result}')

