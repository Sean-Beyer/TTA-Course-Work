using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using StarfinderSRDModelBinding.Models;

namespace StarfinderSRD
{
    public partial class AddCharacter : System.Web.UI.Page
    {
        public void addCharacterForm_InsertItem()
        {
            var item = new Character();

            TryUpdateModel(item);
            if (ModelState.IsValid)
            {
                using (CharacterContext db = new CharacterContext())
                {
                    db.Characters.Add(item);
                    db.SaveChanges();
                }
            }
        }

        protected void cancelButton_Click(object sender, EventArgs e)
        {
            Response.Redirect("~/Characters");
        }

        protected void addCharacterForm_ItemInserted(object sender, FormViewInsertedEventArgs e)
        {
            Response.Redirect("~/Characters");
        }

        protected void Page_Load(object sender, EventArgs e)
        {

        }
    }
}