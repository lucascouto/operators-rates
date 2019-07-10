# operators-rates

## What this is about

  Some telephone operators have submitted their price lists including price per minute for different phone number prefixes. The price lists look like this:
  
  <table>
    <tr>
      <td colspan="2"><strong>OPERATOR A</strong></td>
    </tr>
    <tr>
      <td><strong>Prefix</strong></td>
      <td><strong>Rate ($/min)</strong></td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>268</td>
      <td>5.1</td>
    </tr>
    <tr>
      <td>46</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>4620</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>468</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>4631</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>4673</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>46732</td>
      <td>1.1</td>
    </tr>
</table>

<table>
    <tr>
      <td colspan="2"><strong>OPERATOR B</strong></td>
    </tr>
    <tr>
      <td><strong>Prefix</strong></td>
      <td><strong>Rate ($/min)</strong></td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <td>44</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>46</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>467</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>48</td>
      <td>1.2</td>
    </tr>
</table>

The left column represents the telephone prefix (country + area code) and the right column represents the operators price per minute for a number starting with that prefix. When several prefixes match the same number, the longest one should be used. If you, for example, dial +46-73-212345 you will have to pay $ 1.1/min with Operator A and $ 1.0/min with Operator B. 

If a price list does not include a certain prefix you cannot use that operator to dial numbers starting with that prefix. For example it is not possible to dial +44 numbers with operator A but it is possible with Operator B.

This Python program can handle any number of price lists (operators) and then can calculate which operator that is cheapest for a certain number. Each price list can have thousands of entries.

