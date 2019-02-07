UI
--

******** wx viewer should be part of osvcad (coming from aocutils)
  ******** AUI or split window for UI (shelf + 3d + graph)
  ******** integrate the graph viewer
  ******** Set the assembly in the model to do the first tests
  ******** callbacks for selections in the ui
  ******** MVC pattern using Atom + move away from calling the UI in nodes or assemblies
  ******** Anchors display (and selectable)
  ******** Live part coding (editor and viewer side by side)

******** Add a tree panel to display the files and folders under the script

******** Automatic update of views upon selection in tree
******** Update code display upon file selection

******** Open a folder, not a script - then select something to display

******** Wait message upon 3d display loading (BusyInfo)

******** Save button for modified Python files

******** Make sure view_* functions are under if __main__ for sample projects

******** Redirect output to a window

******** Adapt display to selected file + change Lexer in editor
  Python
    regular python file
    python file with assembly
    python file with part
    part script python file
  CAD (STEP, IGES, STL ...) -> code display when ascii + 3d display
  STEPZIP -> no code display, but 3d viewable
  Binary files ->
  JSON -> change lexer
    regular json library definition file

******** Display of parts libraries

******** Better anchors display

******** Selecting a part definition python script (see test_project) does not update the 3d viewer

******** Display of anchor names

******** Graph display

******** Assemblies should display their anchors too
  Transparency needs to be adjustable on the fly as some anchors/anchor names could be hidden
  OR use wireframe mode !!

******** Launch with command line
     ****** create bin that launches ui
     ****** conda package (0.6.0)
     ****** bin defined in setup
     ****** needs sys.exit() to exit process when closed (does not return to command prompt when closed otherwise)

******** Require an explicit Open (no more project default dir)

******** 3D display of graph with nodes position based on barycentre

******** color sequence so that a part and its corresponding display (sphere) in the graph view have the same colour

******** scaling of spheres -> based on BB of parts (a part may have no volume)
