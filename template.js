    [
        {
        	'title': 'Fashion and Style',
        	'link': 'http://google.com',
         	'submenus':
	        	[
	        		{
	        			'title': 'Featured',
	        			'link': 'http://google.com',
	        			'sections': 
	        			[
	        				{
	        					'section_type': 'products',
	        				 	'items': 
	        				 		[
	        				 			{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		 	{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		 	{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		 	{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		]
	        				}
	        			]
	        		}
	        	]
	    },
	    {
        	'title': 'Beauty & Wellness',
        	'link': 'http://google.com',
         	'submenus':
	        	[
	        		{
	        			'title': 'Featured',
	        			'link': 'http://google.com',
	        			'sections': 
	        			[
	        				{
	        					'section_type': 'products',
	        				 	'items': 
	        				 		[
	        				 			{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		 	{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		 	{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		 	{'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'},
	        				 		]
	        				}
	        			]
	        		}
	        	]
	    }
	]

menu_item = {'title': 'Fashion and Style', 'link': 'http://google.com', 'submenus': []}
submenu_item = {'title': 'Featured', 'link': 'http://google.com', 'sections': []}
sections_item = {'section_type': 'products', 'items':[product_item|article_item|category_item]}

---
product_item = {'link': 'http://google.com', 'pic': 'http://google.com', 'price': 2321, 'title': 'Hallo World'}
article_item = {'link': 'http://google.com', 'pic': 'http://google.com', 'title': 'Hallo World'}
category_item = {'link': 'http://google.com', 'title': 'Hallo World'}


'menu document'
'"menu" collection'

{
	"_id": XXX,
 	"menu": [
 				{
 					'title': 'Fashion and Style',
 		   			'link': 'http://google.com',
 		   			'submenus': [id, id, id]
 		   		},
 		   		{
 		   			'title': 'Beauty & Wellness',
 		   			'link': 'http://google.com',
 		   			'submenus': [id, id, id]
 		   		},
 		   	]
}





"menu_item"
{
	'order': 1,
	'title': 'Fashion and Style',
	'link': 'http://google.com',
	'submenus': [id, id, id]
}



"submenu_item"
{
	'_id': XXX,
	'title': 'Featured',
 	'link': 'http://google.com',
 	'sections': [id, id, id]
}

"submenumenu_section_item"
{
	'_id': XXX,
	'title': 'Featured',
 	'link': 'http://google.com',
 	'sections': [id]	
}

"section_item"
{
	'_id': XXX,
	'section_type': 'products',
	'items':[product_id|article_id|category_id]
}






{
	'_id': XXX,
	'order': 1,
	'title': 'Fashion and Style',
	'link': 'http://google.com',
	'submenus': [
	{
		'title': 'Featured',
	 	'link': 'http://google.com',
	 	'sections': [
	 	{
			'section_type': 'products',
			'items':[product_id|article_id|category_id]
		},
		{
			
			'section_type': 'products',
			'items':[product_id|article_id|category_id]
		}]
	},
	{
		'title': 'Something Else',
	 	'link': 'http://google.com',
	 	'sections': [
		{
			'section_type': 'products',
			'items':[product_id|article_id|category_id]
		},
		{
			'section_type': 'products',
			'items':[product_id|article_id|category_id]
		}]
	}
	]
}
