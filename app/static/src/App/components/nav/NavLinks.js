const NAV_ITEMS = [
  {
    label: "Dashboard",
    href: "/dashboard",
    children: [
      {
        label: "Dedicated",
        subLabel: "Catered towards your usage",
        href: "/dashboard",
      },
    ],
  },
  {
    label: "Trends",
    href: "/trends",
    children: [
      {
        label: "Commodity",
        subLabel: "Change in consumption",
        href: "/trends",
      },
    ],
  },
  {
    label: "Persona",
    href: "/persona",
    children: [
      {
        label: "Persona",
        subLabel: "Change in persona's preferences",
        href: "/persona",
      },
    ],
  },
  {
    label: "Train",
    href: "/train",
  },
];

export default NAV_ITEMS;
