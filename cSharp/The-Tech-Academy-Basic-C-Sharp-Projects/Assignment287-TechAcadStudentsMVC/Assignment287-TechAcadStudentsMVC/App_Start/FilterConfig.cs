using System.Web;
using System.Web.Mvc;

namespace Assignment287_TechAcadStudentsMVC
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }
    }
}
