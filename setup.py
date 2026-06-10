# pip install cx_freeze
import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(
                   script="main.py", 
                   icon="base/icone.png",
                    target_name="HighwayDodgers.exe"
                   ) ]
cx_Freeze.setup(
    name = "Highway Dodgers",
    options={
        "build_exe":{
            "packages":["pygame", "recursos"],
            "include_files":["base"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi