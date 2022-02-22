from tasks import divide_by_zero, divide_by_zero_with_custom_task, divide_by_zero_with_custom_on_failure

divide_by_zero.apply_async(queue='demo')
divide_by_zero_with_custom_task.apply_async(queue='demo')
divide_by_zero_with_custom_on_failure.apply_async(queue='demo')
