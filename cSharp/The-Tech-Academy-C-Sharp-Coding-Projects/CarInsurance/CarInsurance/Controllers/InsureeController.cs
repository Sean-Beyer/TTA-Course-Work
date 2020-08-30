using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using CarInsurance.Models;

namespace CarInsurance.Controllers
{
    public class InsureeController : Controller
    {
        private InsuranceEntities db = new InsuranceEntities();

        // GET: Insuree
        public ActionResult Index()
        {
            return View(db.Insurees.ToList());
        }

        // GET: Insuree/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Insuree insuree = db.Insurees.Find(id);
            if (insuree == null)
            {
                return HttpNotFound();
            }
            return View(insuree);
        }

        // GET: Insuree/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Insuree/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "Id,FirstName,LastName,EmailAddress,DateOfBirth,CarYear,CarMake,CarModel,DUI,SpeedingTickets,CoverageType,Quote")] Insuree insuree)
        {
            if (ModelState.IsValid)
            {
                decimal quoteCalc = 50m;

                //Today's Date
                var today = DateTime.Today.Year;

                //Customers date of birth
                int dobYear = insuree.DateOfBirth.Year;
                int Age = today - dobYear;

                //Age ranges for insurance
                //18
                bool eightTeen = Age <= 18;
                if (eightTeen == true)
                {
                    quoteCalc += 100;
                }

                //getting age range 19 to 25
                bool nineTeen = Age >= 19;
                bool yongerTwentyFive = Age <= 25;
                if (nineTeen == true && yongerTwentyFive == true)
                {
                    quoteCalc += 50;
                }

                //25+
                bool oldTwentyFive = Age >= 26;
                if (oldTwentyFive == true)
                {
                    quoteCalc += 25;
                }

                //Car Year Quotes
                if (insuree.CarYear <= 2000)
                {
                    quoteCalc += 25;
                }
                else if (insuree.CarYear >= 2015)
                {
                    quoteCalc += 25;
                }

                //Car Model Quotes
                // Porche
                var Make = insuree.CarMake;
                if ( Make == "Porche")
                {
                    quoteCalc += 25;
                }

                //Porche & 911
                var Model = insuree.CarModel;
                if (Make == "Porche" && Model == "911 Carrera")
                {
                    quoteCalc += 25;
                }

                //SpeedingTickets Quote
                int PerTicket = insuree.SpeedingTickets * 10;
                {
                    quoteCalc += PerTicket;
                }

                //DUI
                if (insuree.DUI) 
                {
                    quoteCalc += (quoteCalc * .25m);
                }

                //Coverage
                if (insuree.CoverageType)
                {
                    quoteCalc += (quoteCalc * .50m);
                }

                insuree.Quote = quoteCalc;

                db.Insurees.Add(insuree);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(insuree);
        }

        // GET: Insuree/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Insuree insuree = db.Insurees.Find(id);
            if (insuree == null)
            {
                return HttpNotFound();
            }
            return View(insuree);
        }

        // POST: Insuree/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id,FirstName,LastName,EmailAddress,DateOfBirth,CarYear,CarMake,CarModel,DUI,SpeedingTickets,CoverageType,Quote")] Insuree insuree)
        {
            if (ModelState.IsValid)
            {
                db.Entry(insuree).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(insuree);
        }

        // GET: Insuree/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Insuree insuree = db.Insurees.Find(id);
            if (insuree == null)
            {
                return HttpNotFound();
            }
            return View(insuree);
        }

        // POST: Insuree/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Insuree insuree = db.Insurees.Find(id);
            db.Insurees.Remove(insuree);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        // GET: Admin
        public ActionResult Admin()
        {
            return View(db.Insurees.ToList());
        }
    }
}
