import cmd
import os
import importlib
import glob
import signal

class ModularShell(cmd.Cmd):
  intro = "Welcome to the Yoyo Shell. Type 'help'`` or '?' to list commands.\n"
  prompt = "(yoyo) >> "
  modules = {}
  modules_help = {}
  
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.load_commands()

  def load_commands(self):
    command_files = glob.glob("commands/*.py")
    
    for file in command_files:
      module_name = os.path.splitext(os.path.basename(file))[0]
      
      if module_name == "__init__":
        continue
      
      module = importlib.import_module(f"commands.{module_name}")
      
      if module.__doc__:
        self.modules_help[module_name] = module.__doc__.strip()
      else:
        self.modules_help[module_name] = "No help available for this command."
      
      self.modules[module_name] = module
      
      command_func = getattr(module, "execute", None)
      if command_func:
        self.add_command(module_name, command_func)

  
  def get_help(self, command_name=None):
      """Retrieves help information for a specific command or all commands."""
      if command_name:
          return self.help_docs.get(command_name, "No help available for this command.")
      else:
          return "\n".join(f"{name}: {help_text}" for name, help_text in self.help_docs.items())
  
  def add_command(self, name, func):
    def wrapper(arg):
      func(arg)

    setattr(self, f"do_{name}", wrapper)
    
    def help_wrapper():
      print(self.modules_help.get(name, "No help available for this command."))

    setattr(self, f"help_{name}", help_wrapper)

  
  def do_exit(self, arg):
    print("BIBI GO BYEBYE!")
    return True
  
if __name__ == "__main__":
    ModularShell().cmdloop()