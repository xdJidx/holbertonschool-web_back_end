export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;
  
  if (trueOrFalse) {
    const task = true; // Use let instead of var
    const task2 = false; // Use let instead of var
  }
  
  return [task, task2];
}
