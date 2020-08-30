@Imports Web_and_Animation_project.Areas.HelpPage.ModelDescriptions
@ModelType CollectionModelDescription
@If TypeOf Model.ElementDescription Is ComplexTypeModelDescription Then
    @Html.DisplayFor(Function(m) m.ElementDescription)
End If